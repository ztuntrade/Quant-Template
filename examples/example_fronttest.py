import pandas as pd
import requests
import datetime
import pytz
from typing import Union
from untrade.client import Client


def process_data(data):
    """
    Process raw data to calculate moving averages and generate buy/sell signals.

    Parameters:
    - data (DataFrame): Raw data containing 'close' prices.

    Returns:
    - data (DataFrame): Processed data with additional columns for short and long moving averages,
                        and buy/sell signals.
    """
    # Calculate short and long moving averages
    data["Short_MA"] = data["close"].rolling(window=1).mean()
    data["Long_MA"] = data["close"].rolling(window=7).mean()

    # Generate buy/sell signals based on crossover
    data["Signal"] = 0
    data.loc[data["Short_MA"] > data["Long_MA"], "Signal"] = 1
    data.loc[data["Short_MA"] < data["Long_MA"], "Signal"] = -1
    return data


def strat(data):
    """
    Apply strategy to filter consecutive signals.

    Parameters:
    - data (DataFrame): Dataframe containing buy/sell signals.

    Returns:
    - data (DataFrame): Dataframe with filtered signals.
    """
    signal = []
    prev = None
    for value in data["Signal"]:
        # Filter consecutive signals
        if value == prev:
            signal.append(0)
        else:
            signal.append(value)
        prev = value

    data["signals"] = signal
    return data


def fetch_historical_data(
    symbol: str,
    interval: str,
    timezone: Union[None, str] = None,
    startTime: Union[None, str] = None,
    endTime: Union[None, str] = None,
    limit: str = 1000,
    futures: bool = False,
    cm=False,
) -> pd.DataFrame:
    """
    Fetch historical price data from Binance API.

    Parameters:
    - symbol (str): Cryptocurrency symbol (e.g., BTCUSDT).
    - interval (str): Time interval for data (e.g., '1h', '4h', '1d').
    - timezone (str): Timezone to convert timestamps to (optional).
    - startTime (str): Start time for data retrieval (optional).
    - endTime (str): End time for data retrieval (optional).
    - limit (int): Limit the number of data points fetched.
    - futures (bool): Whether to fetch futures data.
    - cm (bool): Not used.

    Returns:
    - data (DataFrame): Historical price data.
    """
    if not futures:
        URL = (
            f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
        )
    else:
        URL = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={interval}"

    if startTime:
        startTime = str(
            int(
                datetime.datetime.timestamp(
                    datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
                )
            )
            * 1000
        )
        URL += f"&startTime={startTime}"
        URL += f"&limit={limit}"
    elif startTime and endTime:
        startTime = str(
            int(
                datetime.datetime.timestamp(
                    datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
                )
            )
            * 1000
        )
        endTime = str(
            int(
                datetime.datetime.timestamp(
                    datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
                )
            )
            * 1000
        )
        URL += f"&startTime={startTime}&endTime={endTime}"
    else:
        URL += f"&limit={limit}"
    response = requests.get(URL, timeout=10)
    data = response.json()

    # Organizing the data
    data_dict = {
        "datetime": [],
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
    }

    for candle in data:
        timestamp = candle[0] / 1000.0
        dt = datetime.datetime.fromtimestamp(timestamp)
        if timezone:
            dt = dt.astimezone(pytz.timezone(timezone))  # Convert to specified timezone

        # Extract OHLCV data from the request data
        O, H, L, C, V = map(float, candle[1:6])

        # Append data to data_dict
        data_dict["datetime"].append(dt)
        data_dict["open"].append(O)
        data_dict["high"].append(H)
        data_dict["low"].append(L)
        data_dict["close"].append(C)
        data_dict["volume"].append(V)

    df = pd.DataFrame(data_dict)
    return df


def fronttest(data):
    """
    Perform fronttesting using generated signals.

    Parameters:
    - data (DataFrame): Dataframe containing buy/sell signals.
    """
    generated_signal_column = "signals"
    client = Client()

    flag = 0
    # Iterate through signals in reverse order
    for i in range(len(data) - 1, -1, -1):
        if data.iloc[i].signals == 1:
            # Buy signal
            if flag == 0:
                print(data.iloc[i]["datetime"], "BUY")
                client.create_order()
                flag = 1
            elif flag == -1:
                print(data.iloc[i]["datetime"], "SQUARED OFF")
                client.close_order()
                flag = 0
            break
        if data.iloc[i].signals == -1:
            # Sell signal
            if flag == 0:
                print(data.iloc[i]["datetime"], "SELL")
                client.create_order()
                flag = 1
            elif flag == 1:
                print(data.iloc[i]["datetime"], "SQUARED OFF")
                client.close_order()
                flag = -1
            break


if __name__ == "__main__":
    # Fetch historical price data
    data = fetch_historical_data(symbol="BTCUSDT", interval="1h", limit=1000)
    if data is not None:
        # Process data
        data = process_data(data)
        data = strat(data)
        # Perform fronttesting
        fronttest(data)
    else:
        print("Data fetching failed.")
