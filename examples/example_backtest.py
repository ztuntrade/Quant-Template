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
        jupyter_id="Your_Jupyter_ID",  # the one you use to login to jupyter.untrade.io
        result_type="Q",
    )
    # result_type can be one of the following:
    # "Q" - Quarterly Analysis(last dates of quarters)
    # "QS" - Quarterly Analysis(start dates of quarters)
    # "M" -  Monthly Analysis(last date of months)
    # "MS"- Monthly Analysis(start dates of months)
    # "Y" - Yearly Analysis(last dates of years)
    # "YS" - Yearly Analysis(start dates of years)
    # "6M" - Semi Annual Analysis(last dates of 6 months)
    # "6MS" - Semi Annual Analysis(start dates of 6 months)

    return result


if __name__ == "__main__":
    csv_file_path = "file_to_check.csv"
    backtest_result = perform_backtest(csv_file_path)
    for value in backtest_result:
        print(value)
