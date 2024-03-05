import pandas as pd
import talib
from untrade.client import Client  # import SDK for backtesting
from pprint import pprint
import multiprocessing


class SMACrossoverStrategy:
    def __init__(self, data):
        self.data = data
        self.short_window = 2
        self.long_window = 2

    def generate_signals(self):

        self.data["Short_SMA"] = talib.SMA(
            self.data["close"], timeperiod=self.short_window
        )
        self.data["Long_SMA"] = talib.SMA(
            self.data["close"], timeperiod=self.long_window
        )

        # Generate buy/sell signals based on crossover
        self.data["Signal"] = 0
        self.data.loc[self.data["Short_SMA"] > self.data["Long_SMA"], "Signal"] = 1
        self.data.loc[self.data["Short_SMA"] < self.data["Long_SMA"], "Signal"] = -1

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


def backtest():
    csv_file_path = "test-2 (1).csv"
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

    # Perform backtest
    client = Client()
    result = client.backtest(file_path=file_path)
    return result


def fronttest():

    # data=#your live data source
    generated_signal_column = "signals"
    client = Client()

    flag = 0
    for i in range(data.shape[0], -1, -1):
        if data.iloc[i, :].signals == 1:
            if flag == 0:
                print(data.iloc[i, :]["datetime", "signals"], " BUY")
                client.create_order()
                flag = 1

            elif flag == -1:
                print(data.iloc[i, :]["datetime", "signals"], " SQUARED OFF")
                client.close_order()
                flag = 0

            break
        if data.iloc[i, :].signals == -1:
            if flag == 0:
                print(data.iloc[i, :]["datetime", "signals"], " SELL")
                client.create_order()
                flag = 1

            elif flag == 1:
                print(data.iloc[i, :]["datetime", "signals"], " SQUARED OFF")
                client.close_order()
                flag = -1

            break


if __name__ == "__main__":
    backtest_process = multiprocessing.Process(target=backtest)
    fronttest_process = multiprocessing.Process(target=fronttest)

    backtest_process.start()
    fronttest_process.start()

    backtest_process.join()
