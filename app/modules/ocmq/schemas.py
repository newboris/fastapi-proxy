from pydantic import BaseModel, Field
from typing import Optional

class RequestBase(BaseModel):
    title: str = Field(..., example="Сломался принтер")
    description: Optional[str] = Field(None, example="Не включается в сеть")

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    additional_info: str = Field(..., example="Проверили кабель, он исправен")

class RequestResponse(RequestBase):
    id: str = Field(..., example="REQ-12345")
    status: str = Field(..., example="IN_PROGRESS")
