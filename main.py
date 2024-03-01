# Refer Examples for more details

import multiprocessing
import time


def backtest():
    # User should write their backtest logic here.
    # Run backtest logic here. This is just a placeholder loop for demonstration.
    print("Backtest started")


def fronttest():
    # User should write their fronttest logic here.
    # This function should be designed to run continuously.
    print("Fronttest started")


if __name__ == "__main__":
    backtest_process = multiprocessing.Process(target=backtest)
    fronttest_process = multiprocessing.Process(target=fronttest)

    backtest_process.start()
    fronttest_process.start()

    backtest_process.join()

    # Note: The fronttest process will keep running.
