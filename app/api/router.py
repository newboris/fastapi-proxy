from fastapi import APIRouter
from app.modules.ocmq.router import router as ocmq_router
# from app.modules.ocml.router import router as ocml_router

api_router = APIRouter()

# Объединяем модули под понятными префиксами и тегами для Swagger
api_router.include_router(ocmq_router, prefix="/ocmq", tags=["Запросы (OCMQ)"])
# api_router.include_router(ocml_router, prefix="/ocml", tags=["Наряды (OCML)"])
