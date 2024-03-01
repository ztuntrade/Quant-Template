#target order
from untrade.client import Client
from pprint import pprint

# Instantiate the client globally
client = Client()

def create_target_order():
    try:
        response = client.create_target_order(
            symbol="BTCUSDT",
            type="TAKE_PROFIT_MARKET",
            market="COIN-M",
            stop_price=45000,
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
        )
        print("target created Successfully:")
        pprint(response)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def create_stoploss_order():
    try:
        response = client.create_stoploss_order(
            symbol="BTCUSDT",
            type="STOP_MARKET",
            market="COIN-M",
            stop_price=35000,
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
        )
        print("stoploss created successfully:")
        pprint(response)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def close_existing_order():
    try:
        response = client.close_order(
            symbol="BTCUSDT",
            market="COIN-M",
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
        )
        print("Order closed successfully:")
        pprint(response)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Calling functions
create_target_order()
create_stoploss_order()
close_existing_order()


#### Parameters
# - `symbol` (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
# - `side` (string): 'BUY' or 'SELL'.
# - `type` (string): 'LIMIT' or 'MARKET'.
# - `market` (string): 'SPOT', 'COIN-M', or 'USD-M'.
# - `quantity` (float, optional): Trade quantity.
# - `price` (float, optional): Entry price (for LIMIT orders).
# - `parent_order_id` (string): The ID of the parent order being closed.