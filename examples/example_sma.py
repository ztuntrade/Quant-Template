import pandas as pd
from untrade.client import Client
import multiprocessing


# Define a strategy class for SMA (Simple Moving Average) crossover
class SMACrossoverStrategy:
    def __init__(self, data):
        self.data = data
        self.short_window = 1
        self.long_window = 7

    def generate_signals(self):
        # Calculate short and long moving averages
        self.data["Short_MA"] = (
            self.data["close"].rolling(window=self.short_window).mean()
        )
        self.data["Long_MA"] = (
            self.data["close"].rolling(window=self.long_window).mean()
        )

        # Generate buy/sell signals based on crossover
        self.data["Signal"] = 0
        self.data.loc[self.data["Short_MA"] > self.data["Long_MA"], "Signal"] = 1
        self.data.loc[self.data["Short_MA"] < self.data["Long_MA"], "Signal"] = -1

        # Generate a new signal column to filter consecutive equal signals
        signals = []
        prev = None
        for value in self.data["Signal"]:
            if value == prev:
                signals.append(0)
            else:
                signals.append(value)
            prev = value

        self.data["generated_signal"] = signals

    def get_signals(self):
        self.generate_signals()
        return self.data["generated_signal"]


# Function for backtesting the strategy
def backtest():
    csv_file_path = "YOUR_CSV"  # Replace with the path to your CSV file
    data = pd.read_csv(csv_file_path)
    short_window = 1
    long_window = 7
    strategy = SMACrossoverStrategy(data)
    strategy.short_window = short_window
    strategy.long_window = long_window
    signals = strategy.get_signals()

    # Save the signals to a new CSV file
    data_with_signals = pd.concat([data, signals], axis=1)
    file_path = "backtest_data.csv"
    data_with_signals.to_csv(file_path, index=False)

    # Perform backtest using a trading API client
    client = Client()
    result = client.backtest(
        jupyter_id="Your_Jupyter_ID",  # the one you use to login to jupyter.untrade.io,
        file_path=file_path,
    )
    return result


# Function for fronttesting the strategy with live data
def fronttest():
    # data = # your live data source
    generated_signal_column = "generated_signal"  # Corrected the column name
    client = Client()

    flag = 0
    for i in range(
        data.shape[0] - 1, -1, -1
    ):  # Iterate through the data in reverse order
        if data.iloc[i, :][generated_signal_column] == 1:
            if flag == 0:
                print(data.iloc[i, :]["datetime"], " BUY")
                client.create_order()
                flag = 1
            elif flag == -1:
                print(data.iloc[i, :]["datetime"], " SQUARED OFF")
                client.close_order()
                flag = 0
            break

        if data.iloc[i, :][generated_signal_column] == -1:
            if flag == 0:
                print(data.iloc[i, :]["datetime"], " SELL")
                client.create_order()
                flag = 1
            elif flag == 1:
                print(data.iloc[i, :]["datetime"], " SQUARED OFF")
                client.close_order()
                flag = -1
            break


if __name__ == "__main__":
    # Create separate processes for backtesting and fronttesting
    backtest_process = multiprocessing.Process(target=backtest)
    fronttest_process = multiprocessing.Process(target=fronttest)

    # Start the processes concurrently
    backtest_process.start()
    fronttest_process.start()

    # Wait for both processes to finish before exiting
    backtest_process.join()
