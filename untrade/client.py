import os
import requests
from typing import Dict, Any, Optional
from untrade.base import BaseClient


class Client(BaseClient):
    def __init__(self, KEY: Optional[str] = None) -> None:
        super().__init__(KEY)

    def _init_session(self) -> requests.Session:
        headers = self._get_headers()

        session = requests.session()
        session.headers.update(headers)
        return session

    def _file_init_session(self) -> requests.Session:
        return requests.session()

    @staticmethod
    def _handle_response(response: requests.Response):
        return response.json()

    @staticmethod
    def _handle_response_stream(response: requests.Response):
        if response.headers["Content-Type"] == "application/json":
            return response.json()
        if response.status_code == 200:
            for line in response.iter_content(chunk_size=1024):
                if line:
                    yield line.decode("utf-8")
        return "BACKTEST FAILED"

    def _handle_file(self, path, file_path, **kwargs):
        uri = self._create_api_uri(path)
        data = self._get_keyword_argumets(**kwargs)
        try:
            files = [
                (
                    "file",
                    (os.path.basename(file_path), open(file_path, "rb"), "text/csv"),
                )
            ]

            self.response = self.file_session.post(
                uri, files=files, data=data, stream=True
            )
            if self.response.status_code >= 400 and self.response.status_code < 500:
                return self._handle_response(
                    self.file_session.post(uri, files=files, data=data)
                )
            return self._handle_response_stream(self.response)
        except FileNotFoundError:
            return None

    def _create_request(self, request_type, path, **kwargs):
        uri = self._create_api_uri(path)
        data = self._get_keyword_argumets(**kwargs)
        self.response = getattr(self.session, request_type)(uri, json=data)
        return self._handle_response(self.response)

    def _get(self, path, **kwargs) -> Any:
        return self._create_request("get", path, **kwargs)

    def _post(self, path, **kwargs) -> Dict:
        return self._create_request("post", path, **kwargs)

    def _put(self, path, **kwargs) -> Dict:
        return self._create_request("put", path, **kwargs)

    def _delete(self, path, **kwargs) -> Dict:
        return self._create_request("delete", path, **kwargs)

    def create_order(self, **params) -> Dict:
        """
        Creates an order with the provided parameters.

        Parameters:
            symbol (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
            side (string): The side of the order, either 'BUY' or 'SELL'.
            type (string): The type of the order, either 'LIMIT' or 'MARKET'.
            market (string): The market type, either 'SPOT', 'COIN-M', or 'USD-M'.
            target (float, optional): Target price for the order.
            stop_loss (float, optional): Stop loss price for the order.
            price (float, optional): Entry price for the order (required for LIMIT orders).
            quantity (float, optional): The quantity to trade.
            leverage (int, optional): The leverage for the trade (required for non-SPOT markets).
            position (float, optional): The position size for the trade.

        Important Note
            Either position or quantity must be specified in the request. If both or neither are provided, the API will return an error.
        """
        return self._post(path="untrade/order/create", data=params)

    def close_order(self, **params) -> Dict:
        """
        Closes an order with the provided parameters.

        Parameters:
            symbol (string): The trading symbol (e.g., BTC, ETH).
            market (string): The market type, either 'SPOT', 'COIN-M', or 'USD-M'.
            type (string): The type of the order, either 'LIMIT' or 'MARKET'.
            price (float, optional): The price per unit (required for LIMIT orders).
            quantity (float): The quantity to trade.
            parent_order_id (string): The ID of the parent order being closed.
        """
        return self._post(path="untrade/order/close", data=params)

    def create_target_order(self, **params) -> Dict:
        """
        Creates a target order with the provided parameters.

        Parameters:
            symbol (string): The trading symbol (e.g., BTC, ETH).
            market (string): The market type, either 'SPOT', 'COIN-M', or 'USD-M'.
            type (string): The type of the order, either 'LIMIT' or 'MARKET'.
            price (float, optional): The price per unit (required for LIMIT orders).
            quantity (float): The quantity to trade.
            parent_order_id (string): The ID of the parent order being closed.
        """
        return self._post(path="untrade/order/target", data=params)

    def create_stoploss_order(self, **params) -> Dict:
        """
        Creates a stop-loss order with the provided parameters.

        Parameters:
            symbol (string): The trading symbol (e.g., BTC, ETH).
            market (string): The market type, either 'SPOT', 'COIN-M', or 'USD-M'.
            type (string): The type of the order, either 'LIMIT' or 'MARKET'.
            price (float, optional): The price per unit (required for LIMIT orders).
            quantity (float): The quantity to trade.
            parent_order_id (string): The ID of the parent order being closed.
        """
        return self._post(path="untrade/order/stop-loss", data=params)

    def backtest(self, file_path, **params) -> Dict:
        """
        Runs a backtest with the provided file.

        Parameters:

        file_path (str): Path to the file used for backtesting.

        File Requirements:
            Format: CSV (Comma-Separated Values)
        Content Structure:
            The CSV file must include the following headers in the exact order:
            Index (int)
            datetime (datetime) : Format YYYY-MM-DD HH:MM:SS
            open (float)
            high (float)
            low (float)
            close (float)
            volume (float)
            signals (int)
        Each row in the file should represent a different time point in the dataset.
        """
        return self._handle_file("untrade/backtest-stream", file_path, data=params)

    def fetch_live_data(self, **params) -> Dict:
        """
        Fetches live data for the provided symbol.

        Parameters:
            symbol (string): The trading symbol (e.g., BTCUSDT, ETHUSDT).
            intreval (string): The time interval for the data (e.g., 1m, 5m, 15m, 30m 1h, 4h, 1d).
            limit (int, optional): The number of data points to fetch (max limit is 1000).
        """
        return self._get(path="untrade/ohlc", data=params)
