from typing import Dict


class Config:
    API_URL = "https://api.untrade.io/v1"
    REQUEST_TIMEOUT: float = 60

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance


class BaseClient:
    API_URL = "https://api.untrade.io/v1"
    REQUEST_TIMEOUT: float = 60

    def __init__(self, KEY) -> None:
        self.KEY = KEY
        self.session = self._init_session()
        self.file_session = self._file_init_session()

    def _init_session(self):
        raise NotImplementedError

    def _file_init_session(self):
        raise NotImplementedError

    def _create_api_uri(self, path: str) -> str:
        url = self.API_URL
        return url + "/" + path

    def _get_keyword_argumets(self, **kwargs) -> Dict:
        data = kwargs.get("data", None)
        return data

    def _get_headers(self) -> Dict:
        headers = {"Content-Type": "application/json"}
        if self.KEY:
            headers["Authorization"] = f"Bearer {self.KEY}"
        return headers
