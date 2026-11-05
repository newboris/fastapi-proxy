from fastapi import APIRouter, Depends, status
import requests
from app.api.deps import get_http_client, get_auth_header
from app.modules.ocmq.schemas import RequestCreate, RequestUpdate, RequestResponse
from app.modules.ocmq.services import OcmqService

router = APIRouter()

# Фабричная функция тоже становится обычной (без async)
def get_ocmq_service(
    client: requests.Session = Depends(get_http_client),
    auth: str = Depends(get_auth_header)
) -> OcmqService:
    return OcmqService(http_client=client, auth_header=auth)


@router.post("/take", response_model=RequestResponse, status_code=status.HTTP_201_CREATED)
def take_request_to_work(
    payload: RequestCreate,
    service: OcmqService = Depends(get_ocmq_service)
):
    return service.take_to_work(payload)


@router.put("/{request_id}/info", response_model=RequestResponse)
def add_info_to_request(
    request_id: str,
    payload: RequestUpdate,
    service: OcmqService = Depends(get_ocmq_service)
):
    return service.add_info(request_id, payload)


@router.post("/{request_id}/close", response_model=RequestResponse)
def close_request(
    request_id: str,
    service: OcmqService = Depends(get_ocmq_service)
):
    return service.close_request(request_id)
