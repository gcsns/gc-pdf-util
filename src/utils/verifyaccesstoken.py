from typing import Any, Optional
import json
from enum import Enum
from jwcrypto import jwt, jwk
from fastapi import HTTPException
from requests import get
import configs
from logger import logger

class JwtSubjectType(Enum):
    USER='user'
    CLIENT='client'

class User:
    id: str
    type: str

class VerifiedToken:
    decodedToken: dict[str,Any]
    user: User

class VerifyAccessTokenUtil:
    jwks: Optional[jwk.JWKSet] = None

    def refreshJwks(self):
        jwksUrl = f"{configs.AUTH_SERVER_BASE_URL}{configs.AUTH_SERVER_ENDPOINTS['JWKS_JSON']}"
        self.jwks = jwk.JWKSet.from_json(get(jwksUrl).text)
        logger.debug ('refreshed jwks: %s', self.jwks.export())

    def getJwks(self):
        if not self.jwks:
            self.refreshJwks()
        return self.jwks

    def verifyAccessTokenWithSubjectType(self, token: str, subjectTypes:list[JwtSubjectType]=[JwtSubjectType.CLIENT]):
        if not token:
            raise HTTPException(status_code=401, detail='Authorization token is missing')

        decodedToken = None
        try:
            jwks = self.getJwks()
            JWT = jwt.JWT(jwt=token, key=jwks, algs=['RS256'])
            decodedToken = JWT.claims
            decodedToken = json.loads(decodedToken)
        except Exception as err:
            logger.exception('Token decode failed: %s', err)
            logger.debug('configs.AUTH_SERVER_AUDIENCE: %s', configs.AUTH_SERVER_AUDIENCE)
            logger.debug('configs.AUTH_SERVER_ISSUER: %s', configs.AUTH_SERVER_ISSUER)
            logger.debug('token: %s', token)
            raise HTTPException(status_code=401, detail='Invalid authorization token')

        subjectType: JwtSubjectType | None = None
        for currentSubjectType in subjectTypes:
            if decodedToken.get('sub', '').startswith(currentSubjectType.value):
                subjectType = currentSubjectType
                break

        if not subjectType or not decodedToken.get('sub'):
            raise HTTPException(status_code=401, detail=f"Token must belong to a {', '.join(map(lambda st: st.value,subjectTypes))}")

        return {
            "decodedToken": decodedToken,
            "user": {
                'id': decodedToken['sub'][7:],
                'type': subjectType,
            }
        }
