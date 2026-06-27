from jwt import encode, decode, InvalidTokenError
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from core.config import settings

security_schema = OAuth2PasswordBearer(tokenUrl="/token")

def create_jwt_token(user: dict):
    to_encode = user.copy()
    expiry = datetime.now() + timedelta(minutes=int(settings.JWT_EXPIRE_MINUTES))
    to_encode.update({"exp":expiry})
    token = encode(payload=to_encode, key= settings.PRIVET_KEY, algorithm=settings.JWT_ALGO)
    return token
