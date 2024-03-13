import pandas as pd
import requests
from io import StringIO
from untrade.client import Client
from SMA import process_data, strat


def fetch_data(symbol="BTC", pair="USDT", timeframe="1h", futures=False, limit=1000):
    url = f"https://jarvis.untrade.io/fetch_data?symbol={symbol}&pair={pair}&timeframe={timeframe}&futures={futures}&limit={limit}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return pd.read_csv(StringIO(response.content.decode("utf-8")))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def fronttest(data):
    generated_signal_column = "signals"
    client = Client()

    flag = 0
    for i in range(len(data) - 1, -1, -1):
        if data.iloc[i].signals == 1:
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
    data = fetch_data(
        symbol="BTC", pair="USDT", timeframe="1h", futures=False, limit=1000
    )
    if data is not None:
        data = process_data(data)
        data = strat(data)
        fronttest(data)
    else:
        print("Data fetching failed.")
