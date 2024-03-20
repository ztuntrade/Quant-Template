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
        jupyter_id="your jupyter_id",  # the one you use to login to https://jupyter.untrade.io
        file_path=csv_file_path,
        leverage=1,  # Adjust leverage as needed
    )
    return result


if __name__ == "__main__":
    csv_file_path = "Your-csv"
    backtest_result = perform_backtest(csv_file_path)
    print(backtest_result)
    for value in backtest_result:
        print(value)
