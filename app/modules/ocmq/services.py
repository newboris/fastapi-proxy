import requests
from app.core.config import settings
from app.modules.ocmq.schemas import RequestCreate, RequestUpdate

class OcmqService:
    def __init__(self, http_client: requests.Session, auth_header: str):
        self.client = http_client
        self.headers = {"Authorization": auth_header, "Content-Type": "application/json"}
        self.base_url = f"{settings.EXTERNAL_API_URL}/requests"
        self.timeout = 30.0  # Таймаут в секундах

    def take_to_work(self, payload: RequestCreate) -> dict:
        """Взять запрос в работу (Синхронно)"""
        response = self.client.post(
            f"{self.base_url}/take",
            json=payload.model_dump(), 
            headers=self.headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def add_info(self, request_id: str, payload: RequestUpdate) -> dict:
        """Добавить информацию в запрос (Синхронно)"""
        response = self.client.put(
            f"{self.base_url}/{request_id}/info",
            json=payload.model_dump(),
            headers=self.headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def close_request(self, request_id: str) -> dict:
        """Закрыть запрос (Синхронно)"""
        response = self.client.post(
            f"{self.base_url}/{request_id}/close",
            headers=self.headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
