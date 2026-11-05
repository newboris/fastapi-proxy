from fastapi import Header, HTTPException, status
import requests
from app.core.http_client import http_transport

def get_http_client() -> requests.Session:
    """Гарантирует получение работающей сессии requests"""
    return http_transport.get_session()

def get_auth_header(authorization: str = Header(None)) -> str:
    """Извлекает заголовок Authorization (Basic Auth)"""
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization Header",
            headers={"WWW-Authenticate": "Basic"},
        )
    return authorization
