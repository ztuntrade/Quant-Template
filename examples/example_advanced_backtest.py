import pandas as pd
from untrade.client import Client
from pprint import pprint


def process_data(data, short_window=15, long_window=30):
    # Assuming 'data' is a DataFrame
    data["short_mavg"] = (
        data["close"].rolling(window=short_window, min_periods=1, center=False).mean()
    )
    data["long_mavg"] = (
        data["close"].rolling(window=long_window, min_periods=1, center=False).mean()
    )
    return data


def strat(data):
    data["Signal"] = np.where(
        data["short_mavg"] > data["long_mavg"],
        1,
        np.where(data["short_mavg"] < data["long_mavg"], -1, 0),
    )

    # Remove consecutive duplicates from signals
    data["signals"] = data["Signal"].diff().fillna(0)
    data["signals"] = np.where(data["signals"] != 0, data["Signal"], 0)

    # Randomize the signals
    data["signals"] = data["signals"].apply(
        lambda x: (
            np.random.choice([1, 2])
            if x == 1
            else (np.random.choice([-1, -2]) if x == -1 else 0)
        )
    )

    # Set target prices and stop-loss levels
    data["tp"] = np.where(
        data["signals"] > 0, data["close"] * 1.02, 0
    )  # target price is 2% above the close price for long positions
    data["sl"] = np.where(
        data["signals"] < 0, data["close"] * 0.98, 0
    )  # stop loss is 2% below the close price for short positions

    # Clean up intermediate columns
    data.drop(columns=["Signal"], inplace=True)

    return data


def perform_backtest(csv_file_path):
    """
    Perform backtesting using the untrade SDK.

    Parameters:
    - csv_file_path (str): Path to the CSV file containing historical price data and signals.

    Returns:
    - result (generator): Generator object that yields backtest results.
    """
    # Create an instance of the untrade client
    client = Client()

    # Perform backtest using the provided CSV file path
    result = client.backtest(
        jupyter_id="Your_Jupyter_ID",  # the one you use to login to jupyter.untrade.io
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )

    return result


if __name__ == "__main__":
    # Read data from CSV file
    data = pd.read_csv("to_test.csv")

    # Process data
    res1 = process_data(data)

    # Apply strategy
    res = strat(res1)

    # Save processed data to CSV file
    res.to_csv("processed_data.csv", index=False)

    # Perform backtest on processed data
    csv_file_path = "processed_data.csv"
    backtest_result = perform_backtest(csv_file_path)

    # Get the last value of backtest result
    last_value = None
    for value in backtest_result:
        # print(value)  # Uncomment to see the full backtest result (backtest_result is a generator object)
        last_value = value
    print(last_value)
