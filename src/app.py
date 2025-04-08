from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.verifyaccesstoken import VerifyAccessTokenUtil, VerifiedToken, JwtSubjectType
from routes import health, pdf, video, stream_chat
from fastapi.middleware.cors import CORSMiddleware
from asgi_correlation_id import CorrelationIdMiddleware

app = FastAPI(title='gc-pdf-util service', version='0.0.1')
app.add_middleware(CorrelationIdMiddleware)

origins = [
    "http://localhost",
    "https://document-validation.gamechange.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bearerScheme = HTTPBearer()

verifyAccessTokenUtil = VerifyAccessTokenUtil()

def validateToken(token: Annotated[HTTPAuthorizationCredentials, Depends(bearerScheme)])-> VerifiedToken:
    return verifyAccessTokenUtil.verifyAccessTokenWithSubjectType(token.credentials,subjectTypes=[JwtSubjectType.CLIENT])

app.include_router(health.router, prefix='/api', tags=["Health"])

app.include_router(pdf.router, prefix='/api', dependencies=[Depends(validateToken)], tags=["Pdf"])

app.include_router(video.router, prefix='/api', dependencies=[Depends(validateToken)], tags=["Video"])

app.include_router(stream_chat.router, prefix='/api', dependencies=[Depends(validateToken)], tags=["StreamChat"])