import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

def place_order(client: Client, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Executes the order on the Binance Futures Testnet.
    
    Args:
        client: Authenticated Binance client
        symbol: Trading pair (e.g., BTCUSDT)
        side: BUY or SELL
        order_type: MARKET or LIMIT
        quantity: Order quantity
        price: Price for LIMIT orders (optional for MARKET)
    
    Returns:
        Order response dict on success, None on failure
    """
    try:
        # Log order request details
        logger.info("=" * 70)
        logger.info("ORDER REQUEST SUMMARY")
        logger.info("=" * 70)
        logger.info(f"Symbol:        {symbol}")
        logger.info(f"Side:          {side}")
        logger.info(f"Order Type:    {order_type}")
        logger.info(f"Quantity:      {quantity}")
        logger.info(f"Price:         {price if price else 'Market Price'}")
        
        # Build order parameters
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }

        if order_type == 'LIMIT':
            if price is None:
                raise ValueError("Price must be specified for LIMIT orders.")
            params['price'] = price
            params['timeInForce'] = 'GTC'  # Good Till Cancelled
            logger.info(f"Time in Force: GTC (Good Till Cancelled)")
        
        logger.info("=" * 70)
        logger.info("Sending order to Binance Futures Testnet...")
        
        # Call the futures endpoint
        response = client.futures_create_order(**params)
        
        # Log successful response
        logger.info("=" * 70)
        logger.info("ORDER PLACED SUCCESSFULLY")
        logger.info("=" * 70)
        logger.info(f"Order ID:            {response.get('orderId')}")
        logger.info(f"Status:              {response.get('status')}")
        logger.info(f"Client Order ID:     {response.get('clientOrderId')}")
        logger.info(f"Executed Quantity:   {response.get('executedQty')}")
        logger.info(f"Cumulative Quote Qty: {response.get('cumQuote')}")
        
        if response.get('avgPrice') and response.get('avgPrice') != '0':
            logger.info(f"Average Price:       {response.get('avgPrice')}")
        
        logger.info(f"Commission:          {response.get('commission', 'N/A')}")
        logger.info(f"Commission Asset:    {response.get('commissionAsset', 'N/A')}")
        logger.info("=" * 70)
        
        print("\n✓ Order placed successfully!")
        print(f"  Order ID: {response.get('orderId')}")
        print(f"  Status: {response.get('status')}\n")
            
        return response

    except BinanceAPIException as e:
        error_msg = f"Binance API Error [Status {e.status_code}]: {e.message}"
        logger.error("=" * 70)
        logger.error("ORDER FAILED - BINANCE API ERROR")
        logger.error("=" * 70)
        logger.error(error_msg)
        logger.error("=" * 70)
        print(f"\n✗ API Error: {error_msg}\n")
        
    except BinanceRequestException as e:
        error_msg = f"Binance Request Error: Network issue or invalid request - {str(e)}"
        logger.error("=" * 70)
        logger.error("ORDER FAILED - REQUEST ERROR")
        logger.error("=" * 70)
        logger.error(error_msg)
        logger.error("=" * 70)
        print(f"\n✗ Request Error: {error_msg}\n")
        
    except ValueError as e:
        error_msg = f"Validation Error: {str(e)}"
        logger.error("=" * 70)
        logger.error("ORDER FAILED - VALIDATION ERROR")
        logger.error("=" * 70)
        logger.error(error_msg)
        logger.error("=" * 70)
        print(f"\n✗ Validation Error: {error_msg}\n")
        
    except Exception as e:
        error_msg = f"Unexpected Error: {str(e)}"
        logger.error("=" * 70)
        logger.error("ORDER FAILED - UNEXPECTED ERROR")
        logger.error("=" * 70)
        logger.error(error_msg)
        logger.error("=" * 70)
        print(f"\n✗ Unexpected Error: {error_msg}\n")
        
    return None