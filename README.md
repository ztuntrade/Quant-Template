## Description

This project is an innovative platform where multiple teams collaborate and compete to develop the most profitable quantitative trading strategies. The essence of the project lies in its focus on creating algorithms capable of front-testing or front-running in trading scenarios to maximize returns. 

## Getting Started

### User Registration and Setup
#### Signing Up
- Visit  [jupyter.untrade.io](jupyter.untrade.io) to create an account.
- Complete the signup form with your details.
- Once registered, you will receive a confirmation email. Follow the instructions to verify your account.
#### Logging In and Initial Setup
- Log in to your account on  [jupyter.untrade.io](jupyter.untrade.io).
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

Your contributions should adhere to the project's modular design. While code can be written in any style, the execution of your trading strategy must start through main.py, which contains two essential functions: backtest and fronttest.

#### Backtest Function 
Place your backtesting execution logic here. The backtest function is designed to simulate trading strategies based on historical data to evaluate their potential profitability.

#### Fronttest Function
This function is intended to run continuously, monitoring live market data. Developers should implement logic to print "buy" signals with timestamps for conditions that warrant a purchase and "sell" for conditions that suggest selling.

Users are responsible for writing the logic behind buy and sell conditions. For a strategy to be considered valid, the results generated by the fronttest (live testing) must correspond with those from the backtest (historical testing) for the same period. For instance, if the fronttest runs from day 1 to day 10, all buy and sell signals produced should match the backtest results for days 1 to 10, with a permissible delay of a few seconds for timestamps.

### Docker and CI/CD

**Important:** Modifications to the `Dockerfile` or `gitlab-ci.yml` are not permitted. These files are pre-configured for Docker containerization and GitLab CI/CD pipelines, respectively, and are crucial for the project's automated deployment workflow. Any proposed changes to these configurations must be reviewed and approved by the project maintainers.


