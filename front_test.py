"""
All modules and functions required for front_test should be added in requirements.txt.
"""

import pandas as pd
from untrade.client import Client

# ALL your imports here


def process_data(data):
    """
    Process the input data and return a dataframe with all the necessary indicators and data for making signals.

    Parameters:
    data (pandas.DataFrame): The input data to be processed.

    Returns:
    pandas.DataFrame: The processed dataframe with all the necessary indicators and data.
    """
    return data


# -------STRATEGY LOGIC--------#
def strat(data):
    """
    Create a strategy based on indicators or other factors.

    Parameters:
    - data: DataFrame
        The input data containing the necessary columns for strategy creation.

    Returns:
    - DataFrame
        The modified input data with an additional 'signal' column representing the strategy signals.
    """
    return data


def main():
    """
    symbol (str): The symbol for which to fetch the live data.

    interval (str): The interval for fetching the data. Can be one of the following:
        "1m", "3m", "5m", "15m", "30m", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M".

    limit (int): The limit for the number of data points to fetch.
        This should be according to the lookback period, with a maximum limit of 10000.
        Only completed candles are fetched because incomplete candles can change.
    """
    symbol = "BTCUSDT"
    interval = "1h"
    limit = 1000
    client = Client()
    live_data = client.fetch_live_data(symbol=symbol, interval=interval, limit=limit)
    print(live_data)
    data = pd.DataFrame(live_data)
    processed_data = process_data(data)
    result_data = strat(processed_data)
    print(result_data)


if __name__ == "__main__":
    main()
