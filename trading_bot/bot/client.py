import os
import logging
from binance.client import Client
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def get_client() -> Client:
    """
    Loads credentials from environment variables and returns an authenticated Binance Client.
    
    The client is configured to interact with the Binance Futures Testnet (USDT-M).
    
    Returns:
        Client: Authenticated Binance client pointing to testnet
        
    Raises:
        ValueError: If API credentials are not found in environment variables
    """
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        error_msg = "Missing Binance API credentials. Please check your .env file."
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    logger.info("API credentials loaded from environment")
    
    try:
        # Initialize client with testnet=True to route requests to the testnet endpoints
        # Testnet URL: https://testnet.binancefuture.com
        client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance Futures Testnet client initialized successfully")
        logger.info("Base URL: https://testnet.binancefuture.com")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {str(e)}")
        raise
