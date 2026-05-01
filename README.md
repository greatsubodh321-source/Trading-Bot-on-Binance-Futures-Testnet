# Trading Bot on Binance Futures Testnet

This project implements a simplified trading bot for placing Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Features

- ✅ Place Market and Limit orders on Binance Futures Testnet
- ✅ Support for BUY and SELL sides
- ✅ Input validation for all parameters
- ✅ Comprehensive error handling (API errors, network failures, invalid input)
- ✅ Structured code with separated concerns (client, orders, CLI, validators)
- ✅ Detailed logging of API requests, responses, and errors
- ✅ Clean CLI interface using argparse

## Setup

### 1. Create a Binance Futures Testnet Account

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Register and create an account
3. Generate API credentials from your account settings

### 2. Configure Environment Variables

Create a `.env` file in the `trading_bot` directory with your API credentials:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

### 3. Install Dependencies

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## How to Run

First, navigate to the trading_bot directory:

```bash
cd trading_bot
```

Or run from the parent directory using the path.

### Place a Market Order

```bash
# From trading_bot directory:
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

# From parent directory:
python trading_bot/cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
# From trading_bot directory:
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 30000

# From parent directory:
python trading_bot/cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 30000
```

### Command Line Arguments

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `--symbol` | Yes | Trading pair symbol | `BTCUSDT`, `ETHUSDT` |
| `--side` | Yes | Order direction | `BUY` or `SELL` |
| `--order-type` | Yes | Type of order | `MARKET` or `LIMIT` |
| `--quantity` | Yes | Amount to trade | `0.001`, `1.5` |
| `--price` | No* | Price per unit | `30000`, `1800` |

*Required only for LIMIT orders

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py          # Package initialization
│   ├── client.py            # Binance API client wrapper
│   ├── orders.py            # Order placement logic
│   ├── validators.py        # Input validation
│   └── logging_config.py    # Logging configuration
├── cli.py                   # CLI entry point
├── .env                     # API credentials (not in version control)
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Code Structure

### `bot/client.py`
- Initializes authenticated Binance client
- Loads credentials from `.env` file
- Handles connection to testnet

### `bot/orders.py`
- Executes orders via Binance Futures API
- Handles both MARKET and LIMIT orders
- Comprehensive error handling
- Logs request summary and response details

### `bot/validators.py`
- Validates side (BUY/SELL)
- Validates order type (MARKET/LIMIT)
- Provides clear error messages

### `bot/logging_config.py`
- Sets up logging to both console and file
- Creates `logs/` directory automatically
- Logs all API interactions and errors

### `cli.py`
- Entry point for the application
- Parses command-line arguments
- Orchestrates validation, client initialization, and order placement

## Logging

All logs are written to `logs/trading_bot.log` with the following format:

```
YYYY-MM-DD HH:MM:SS | LOG_LEVEL | MODULE_NAME | MESSAGE
```

Example log output:
```
2024-05-01 10:30:45,123 | INFO | CLI | Initializing Binance Testnet Client...
2024-05-01 10:30:46,234 | INFO | bot.orders | --- Order Request Summary ---
2024-05-01 10:30:46,234 | INFO | bot.orders | Symbol: BTCUSDT | Side: BUY | Type: MARKET | Qty: 0.001 | Price: N/A
2024-05-01 10:30:47,345 | INFO | bot.orders | --- Order Successful ---
2024-05-01 10:30:47,345 | INFO | bot.orders | Order ID: 123456789
```

## Error Handling

The application handles various error scenarios:

- **Invalid Input**: Missing or incorrectly formatted arguments
- **API Errors**: Invalid symbols, insufficient balance, rate limiting
- **Network Errors**: Connection failures or timeouts
- **Validation Errors**: Invalid side/order type combinations

All errors are logged with clear messages to help with debugging.

## Assumptions

- The bot interacts with the **Binance Futures Testnet (USDT-M)** only
- API credentials are provided via `.env` file in the project root
- All quantities and prices must be valid for the specified symbol
- The user has sufficient testnet balance for order placement
- Timestamps are in UTC

## Example Workflow

1. **Set up credentials** in `.env`
2. **Navigate to the trading_bot directory**:
   ```bash
   cd trading_bot
   ```
3. **Run a market order**:
   ```bash
   python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
   ```
4. **Run a limit order**:
   ```bash
   python cli.py --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 2000
   ```
5. **Check logs** in `logs/trading_bot.log` for detailed information

## Troubleshooting

### Missing API Credentials
**Error**: "Missing Binance API credentials. Please check your .env file."
- Ensure `.env` file exists in the project root
- Verify `BINANCE_API_KEY` and `BINANCE_API_SECRET` are set

### Invalid Symbol
**Error**: "Binance API Error: Status 400 - Invalid symbol"
- Use correct trading pair symbols (e.g., `BTCUSDT`, `ETHUSDT`)
- Check [Binance Testnet](https://testnet.binancefuture.com) for available symbols

### Insufficient Balance
**Error**: "Binance API Error: Status 400 - Account has insufficient balance"
- Add funds to your testnet account through the Binance Testnet dashboard

## Dependencies

See `requirements.txt` for a complete list of dependencies:
- `python-binance`: Official Binance Python client
- `python-dotenv`: Environment variable management

## License

This project is for educational purposes only.
