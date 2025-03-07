from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.verifyaccesstoken import VerifyAccessTokenUtil, VerifiedToken, JwtSubjectType
from routes import health, pdf, video
from asgi_correlation_id import CorrelationIdMiddleware

app = FastAPI(title='gc-pdf-util service', version='0.0.1')
app.add_middleware(CorrelationIdMiddleware)


bearerScheme = HTTPBearer()

verifyAccessTokenUtil = VerifyAccessTokenUtil()

def validateToken(token: Annotated[HTTPAuthorizationCredentials, Depends(bearerScheme)])-> VerifiedToken:
    return verifyAccessTokenUtil.verifyAccessTokenWithSubjectType(token.credentials,subjectTypes=[JwtSubjectType.CLIENT])

app.include_router(health.router, prefix='/api', tags=["Health"])

app.include_router(pdf.router, prefix='/api', dependencies=[Depends(validateToken)], tags=["Pdf"])

app.include_router(video.router, prefix='/api', dependencies=[Depends(validateToken)], tags=["Video"])