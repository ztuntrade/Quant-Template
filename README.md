## Description

This project is an innovative platform where multiple teams collaborate and compete to develop the most profitable quantitative trading strategies. The essence of the project lies in its focus on creating algorithms capable of front-testing or front-running in trading scenarios to maximize returns. 

## Getting Started

### User Registration and Setup
#### Signing Up
- Visit  [jupyter.untrade.io](https://jupyter.untrade.io/) to create an account.
- Complete the signup form with your details.
- Once registered, you will receive a confirmation email. Follow the instructions to verify your account.
#### Logging In and Initial Setup
- Log in to your account on  [jupyter.untrade.io](https://jupyter.untrade.io/).
- Upon your first login, please wait for about a minute as the system prepares your workspace.
- After the setup is complete, navigate to the work folder in your dashboard. You will find a template main.py file and any necessary directory structure already created for you.

### Prerequisites (Not for Jupyterhub Users)

- Python >=3.8
- pip3 (Python package manager)

### Installation (Not for Jupyterhub Users)

Clone this repository to your local machine:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```


### Adding Dependencies

If your development introduces new Python packages as dependencies, ensure to list them in the `requirements.txt` file. Format each dependency on a new line, specifying the exact version to maintain consistency across environments:

```
flask==1.1.2
requests==2.25.1
```

### Backtesting with Provided Data Sets
The project includes a data folder containing CSV files with BTCUSDT trading data over various timeframes for the years 2018 through 2022, as well as separate data for 2023. These data sets are a valuable resource for developers looking to backtest their trading strategies against historical price movements and market conditions.

### Untrade SDK
Within the project, you will find an examples folder that contains sample strategies for generating buy and sell signals and performing backtests. These examples serve as a valuable resource for understanding how to effectively utilize the project's structure and the Untrade SDK.

#### Untrade SDK
This SDK is a powerful tool available to users for backtesting trading strategies and generating mock order data. It supports the development process by providing a simplified interface for simulating trading scenarios and validating the effectiveness of strategies. Numerous examples within the examples folder demonstrate how to leverage the Untrade SDK for these purposes.

### Project Structure and Execution

This project is designed to allow users to develop, backtest, and live-test their trading strategies. Users should implement their trading strategies in back_test.py for historical simulation and front_test.py for live monitoring.

#### back_test.py
Place your backtesting execution logic here. This should be designed to simulate trading strategies based on historical data to evaluate their potential profitability.

#### front_test.py
Real-time Signal Generation in front_test.py
In the dynamic environment of quantitative trading, real-time signal generation based on live data plays a pivotal role. To facilitate this, users are required to create a script named front_test.py, which will be responsible for analyzing current market data and making timely trading decisions.

##### Script Requirements
Fetching Historical Data: The script must utilize the fetch_historical_data() function available in the examples folder to retrieve the latest market data each time it runs. This function ensures that the script has access to the most recent data necessary for making informed trading decisions.

##### Timeframe Specification
Users must include a comment at the beginning of the front_test.py script specifying the timeframe they are using for their trading strategy. This is crucial for understanding the context in which the script operates and the frequency of data retrieval. For example:

```
# Timeframe: 15-minute
```
This comment indicates that the strategy analyses data in 15-minute intervals.

#### Decision Making
The core of front_test.py should mirror the decision-making process outlined in back_test.py, allowing for a consistent approach between historical backtesting and real-time analysis. Users should implement logic within front_test.py to decide, at each run, whether to buy, sell, or hold based on the newly fetched data. This involves evaluating the current market conditions against the user's predefined criteria for trading signals.

#### Implementing the Script
The front_test.py script should be structured to execute the following steps:

##### Data Retrieval 
- Call fetch_historical_data() to get the latest available market data.
- Analysis: Analyze the fetched data to apply the trading strategy, using the same logic and conditions as in your backtesting.
- Action Decision: Based on the analysis, the script should print out the action to be taken - "buy", "sell", or "hold" with timeframe, user can also call create_order from SDK

Users are responsible for writing the logic behind buy and sell conditions. For a strategy to be considered valid, the results generated by the fronttest (live testing) must correspond with those from the backtest (historical testing) for the same period. For instance, if the fronttest runs from day 1 to day 10, all buy and sell signals produced should match the backtest results for days 1 to 10, with a permissible delay of a few seconds for timestamps.

**Review Examples**
Before writing your code, review the examples provided in the /examples folder. These examples demonstrate how to structure your backtest and fronttest logic.

**example_backtest.py:** An example showing how to implement a backtest.
**example_frontest.py:** An example showing how to implement a fronttest.

### Installation of TA-LIB
Paste following commands in any jupyter notebook in **work** folder
```bash
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

!tar -xzf ta-lib-0.4.0-src.tar.gz
%cd ta-lib/
!./configure --prefix=$HOME
!make
!make install

!TA_LIBRARY_PATH=~/lib TA_INCLUDE_PATH=~/include pip install ta-lib
```

### Docker and CI/CD

**Important:** Modifications to the `Dockerfile` or `gitlab-ci.yml` are not permitted. These files are pre-configured for Docker containerization and GitLab CI/CD pipelines, respectively, and are crucial for the project's automated deployment workflow. Any proposed changes to these configurations must be reviewed and approved by the project maintainers.


