import pandas as pd
from untrade.client import Client
from pprint import pprint


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
        if value == prev:
            signal.append(0)
        else:
            signal.append(value)
        prev = value

    data["signals"] = signal
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
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )

    return result


if __name__ == "__main__":
    # Read data from CSV file
    data = pd.read_csv("Your_data.csv")

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
