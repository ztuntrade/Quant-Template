from untrade.client import Client
from pprint import pprint


def perform_backtest(csv_file_path):
    """
    Perform backtesting using the untrade SDK.

    Parameters:
    - csv_file_path (str): Path to the CSV file containing historical price data and signals.

    Returns:
    - result (generator): Result is a generator object that can be iterated over to get the backtest results.
    """
    # Create an instance of the untrade client
    client = Client()

    # Perform backtest using the provided CSV file path
    result = client.backtest(
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )

    return result


# Example usage:
csv_file_path = "YOUR_CSV"
backtest_result = perform_backtest(csv_file_path)
last_value = None
for value in backtest_result:
    last_value = value
print(last_value)
## File Requirements

# **Format:** CSV (Comma-Separated Values)

# **Content Structure:** The CSV file must include the following headers in the exact order:

# - Index (int)
# - datetime (datetime) : Format YYYY-MM-DD HH:MM:SS
# - open (float)
# - high (float)
# - low (float)
# - close (float)
# - volume (float)
# - signals (int)

# Each row in the file should represent a different time point in the dataset.


import pandas as pd


def process_data(data):
    data["Short_MA"] = data["close"].rolling(window=1).mean()
    data["Long_MA"] = data["close"].rolling(window=7).mean()

    # Generate buy/sell signals based on crossover
    data["Signal"] = 0
    data.loc[data["Short_MA"] > data["Long_MA"], "Signal"] = 1
    data.loc[data["Short_MA"] < data["Long_MA"], "Signal"] = -1
    return data


def strat(data):
    signal = []
    prev = None
    for value in data["Signal"]:
        if value == prev:
            signal.append(0)
        else:
            signal.append(value)
        prev = value

    data["signals"] = signal
    return data


if __name__ == "__main__":
    data = pd.read_csv("to_test.csv")
    res1 = process_data(data)
    res = strat(res1)
    res.to_csv("processed_data.csv", index=False)

from untrade.client import Client
from pprint import pprint


def perform_backtest(csv_file_path):
    """
    Perform backtesting using the untrade SDK.

    Parameters:
    - csv_file_path (str): Path to the CSV file containing historical price data and signals.

    Returns:
    - result (generator): Result is a generator object that can be iterated over to get the backtest results.
    """
    # Create an instance of the untrade client
    client = Client()

    # Perform backtest using the provided CSV file path
    result = client.backtest(
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )

    return result


if __name__ == "__main__":
    csv_file_path = "processed_data.csv"
    backtest_result = perform_backtest(csv_file_path)
    last_value = None
    for value in backtest_result:
        last_value = value
    print(last_value)
