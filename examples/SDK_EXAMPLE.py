from untrade.client import Client


client = Client()


# Function to create a market order without specifying a target stop loss
def create_order_without_target_stop_loss():
    try:
        # Attempt to create a market order using the specified parameters
        response = client.create_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            side="BUY",  # Order type: BUY (you can also use "SELL" for selling)
            type="MARKET",  # Order type: MARKET (executed immediately at the current market price)
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            quantity=100,  # Quantity of the asset to buy or sell
            leverage=10,  # Leverage level for the order (adjust as needed)
        )
        # Print a success message and display the order response details
        print("Order Created Successfully:")
        print(response, sort_dicts=False)

    except Exception as e:
        # Print an error message if there's an exception during order creation
        print(f"Error creating order: {e}")


# Call the function to execute the order creation
create_order_without_target_stop_loss()


# Function to create a market order with a target and stop loss
def create_market_order_with_target_stop_loss():
    try:
        # Attempt to create a market order using the specified parameters
        response = client.create_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            side="BUY",  # Order type: BUY (you can also use "SELL" for selling)
            type="MARKET",  # Order type: MARKET (executed immediately at the current market price)
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            quantity=100,  # Quantity of the asset to buy or sell
            leverage=10,  # Leverage level for the order (adjust as needed)
            target=45000,  # Target price for the market order
            stop_loss=35000,  # Stop-loss price for the market order
        )
        # Print a success message and display the order response details
        print("Order Created Successfully:")
        print(response, sort_dicts=False)

    except Exception as e:
        # Print an error message if there's an exception during order creation
        print(f"Error creating order: {e}")


# Call the function to execute the market order creation
create_market_order_with_target_stop_loss()


# Function to create a limit order with a target and stop loss
def create_limit_order_with_target_stop_loss():
    try:
        # Attempt to create a limit order using the specified parameters
        response = client.create_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            side="BUY",  # Order type: BUY (you can also use "SELL" for selling)
            type="LIMIT",  # Order type: LIMIT (executed at a specified price or better)
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            quantity=100,  # Quantity of the asset to buy or sell
            leverage=10,  # Leverage level for the order (adjust as needed)
            target=45000,  # Target price for the limit order
            stop_loss=35000,  # Stop-loss price for the limit order
            price=42000,  # Price at which the limit order will be executed or better
        )
        # Print a success message and display the order response details
        print("Order Created Successfully:")
        print(response, sort_dicts=False)

    except Exception as e:
        # Print an error message if there's an exception during order creation
        print(f"Error creating order: {e}")


# Call the function to execute the limit order creation
create_limit_order_with_target_stop_loss()


# Function to create a target order
def create_target_order():
    try:
        # Attempt to create a take profit market order using the specified parameters
        response = client.create_target_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            type="TAKE_PROFIT_MARKET",  # Order type: TAKE_PROFIT_MARKET
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            stop_price=45000,  # Stop price for the take profit order
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8",  # ID of the parent order
        )
        # Print a success message and display the order response details
        print("Target order created Successfully:")
        print(response)
    except Exception as e:
        # Print an error message if there's an exception during order creation
        print(f"An unexpected error occurred: {e}")


# Function to create a stop-loss order
def create_stoploss_order():
    try:
        # Attempt to create a stop market order using the specified parameters
        response = client.create_stoploss_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            type="STOP_MARKET",  # Order type: STOP_MARKET
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            stop_price=35000,  # Stop price for the stop-loss order
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8",  # ID of the parent order
        )
        # Print a success message and display the order response details
        print("Stop-loss order created successfully:")
        print(response)
    except Exception as e:
        # Print an error message if there's an exception during order creation
        print(f"An unexpected error occurred: {e}")


# Function to close an existing order
def close_existing_order():
    try:
        # Attempt to close the specified order using the specified parameters
        response = client.close_order(
            symbol="BTCUSDT",  # Trading pair (Bitcoin to USDT)
            market="COIN-M",  # Market identifier (replace with the correct market if needed)
            parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8",  # ID of the order to be closed
        )
        # Print a success message and display the order response details
        print("Order closed successfully:")
        print(response)
    except Exception as e:
        # Print an error message if there's an exception during order closing
        print(f"An unexpected error occurred: {e}")


# Calling the functions
create_target_order()
create_stoploss_order()
close_existing_order()
