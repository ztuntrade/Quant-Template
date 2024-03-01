#limit order
from untrade.client import Client
from pprint import pprint

client = Client()

def create_limit_order_with_target_stop_loss():
    try:
        response = client.create_order(
            symbol="BTCUSDT",
            side="BUY",
            type="LIMIT",
            market="COIN-M",
            quantity=100,
            leverage=10,
            target=45000,
            stop_loss=35000,
            price=42000
            
        )
        print("Order Created Successfully:")
        pprint(response, sort_dicts=False)

    except Exception as e:
        print(f"Error creating order: {e}")
create_limit_order_with_target_stop_loss()


# Parameters:
# symbol (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
# side (string): 'BUY' or 'SELL'.
# type (string): 'LIMIT' or 'MARKET'.
# market (string): 'SPOT', 'COIN-M', or 'USD-M'.
# quantity (float, optional): Trade quantity.
# leverage (int, optional): Leverage for the trade (for non-SPOT markets).
# target (float, optional): Target price.
# stop_loss (float, optional): Stop loss price.
# price (float, optional): Entry price (for LIMIT orders).
# position (float, optional): Position size.
