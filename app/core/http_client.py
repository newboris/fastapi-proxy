import requests

class HttpClient:
    _session: requests.Session = None

    @classmethod
    def get_session(cls) -> requests.Session:
        """Возвращает единый инстанс сессии (синглтон)"""
        if cls._session is None:
            cls._session = requests.Session()
            # Можно задать глобальные настройки, например таймаут
            # (но в requests таймаут лучше передавать при каждом запросе)
        return cls._session

# Переменная для использования в зависимостях
http_transport = HttpClient()