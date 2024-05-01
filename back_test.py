"""
All modules and functions required for back_test should be added in requirements.txt.
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


def perform_backtest(csv_file_path):
    client = Client()
    result = client.backtest(
        jupyter_id="Your User",  # the one you use to login to jupyter.untrade.io
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )
    return result


def main():
    data = pd.read_csv("data/2018-22/YOUR CSV")

    processed_data = process_data(data)

    result_data = strat(processed_data)

    csv_file_path = "results.csv"

    result_data.to_csv(csv_file_path, index=False)

    backtest_result = perform_backtest(csv_file_path)
    print(backtest_result)
    last_value = None
    for value in backtest_result:
        last_value = value
    print(last_value)


if __name__ == "__main__":
    main()
