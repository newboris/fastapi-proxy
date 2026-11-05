from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # URL внешнего сервиса, куда проксируем запросы
    EXTERNAL_API_URL: str = "https://external-service.com"

    # Настройки самого FastAPI
    PROJECT_NAME: str = "FastAPI Proxy Service"
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
