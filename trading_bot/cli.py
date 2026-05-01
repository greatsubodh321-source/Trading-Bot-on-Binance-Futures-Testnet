import argparse
import logging
from bot.logging_config import setup_logging
from bot.validators import validate_side, validate_order_type, validate_symbol, validate_quantity, validate_price
from bot.client import get_client
from bot.orders import place_order

def main():
    setup_logging()
    logger = logging.getLogger("CLI")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, required=True, help="Order side (BUY or SELL)")
    parser.add_argument('--order-type', type=str, required=True, help="Order type (MARKET or LIMIT)")
    parser.add_argument('--quantity', type=float, required=True, help="Amount to trade")
    parser.add_argument('--price', type=float, default=None, help="Price (Required if type is LIMIT)")

    args = parser.parse_args()

    try:
        # 1. Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        if order_type == 'LIMIT' and price is None:
            parser.error("--price is strictly required when using a LIMIT order.")

        # 2. Initialize Client
        logger.info("Initializing Binance Testnet Client...")
        client = get_client()

        # 3. Place Order
        place_order(client, symbol, side, order_type, quantity, price)

    except ValueError as e:
        logger.error(f"Input Validation Error: {e}")
        exit(1)
    except Exception as e:
        logger.error(f"Fatal Initialization Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()