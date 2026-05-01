# Testing Guide - Trading Bot on Binance Futures Testnet

This guide explains how to test the trading bot and what to expect.

## Prerequisites

1. ✅ Python 3.7+ installed
2. ✅ Binance Futures Testnet account created ([Register here](https://testnet.binancefuture.com))
3. ✅ API credentials generated from testnet account
4. ✅ Dependencies installed: `pip install -r requirements.txt`
5. ✅ `.env` file configured with your credentials

## Setup Steps

### 1. Create Binance Testnet Account

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Click "Register" and create a new account
3. Complete email verification
4. Login to your testnet account

### 2. Generate API Credentials

1. In your testnet account, go to **Account Settings** → **API Management**
2. Click **Create New Key**
3. Complete the verification process
4. You'll receive:
   - API Key
   - Secret Key (save this securely, shown only once)

### 3. Configure .env File

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

### 4. Verify Testnet Balance

1. Login to [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Check your account balance (testnet account typically starts with some balance)
3. If balance is low, you can reset your testnet account

## Running Tests

### Test 1: Check CLI Help

Verify the CLI is working:

```bash
python cli.py --help
```

Expected output:
```
usage: cli.py [-h] --symbol SYMBOL --side SIDE --order-type ORDER_TYPE 
              --quantity QUANTITY [--price PRICE]

Binance Futures Testnet Trading Bot

optional arguments:
  -h, --help            show this help message and exit
  --symbol SYMBOL       Trading pair (e.g., BTCUSDT)
  --side SIDE          Order side (BUY or SELL)
  --order-type ORDER_TYPE
                        Order type (MARKET or LIMIT)
  --quantity QUANTITY   Amount to trade
  --price PRICE         Price (Required if type is LIMIT)
```

### Test 2: Input Validation Tests

#### Missing Required Arguments
```bash
python cli.py --symbol BTCUSDT
```
Expected: Error showing missing required arguments

#### Invalid Order Type
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type INVALID --quantity 0.001
```
Expected: `Input Validation Error: Invalid order type. Must be 'MARKET' or 'LIMIT'.`

#### Invalid Side
```bash
python cli.py --symbol BTCUSDT --side INVALID --order-type MARKET --quantity 0.001
```
Expected: `Input Validation Error: Invalid side. Must be 'BUY' or 'SELL'.`

#### Negative Quantity
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity -0.001
```
Expected: `Input Validation Error: Quantity must be greater than 0.`

#### LIMIT Order without Price
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001
```
Expected: Error about missing --price argument

### Test 3: Successful Market Order (LIVE TEST)

⚠️ This will place a **real order** on the testnet!

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

Expected output:
```
✓ Order placed successfully!
  Order ID: 1234567890
  Status: FILLED

Log file: logs/trading_bot.log
```

Check the log file:
```bash
cat logs/trading_bot.log
```

You should see:
- Order request summary
- Order response with Order ID
- Status: FILLED (market orders usually fill immediately on testnet)
- Average price

### Test 4: Successful Limit Order (LIVE TEST)

⚠️ This will place a **real order** on the testnet!

```bash
python cli.py --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 2000
```

Expected output:
```
✓ Order placed successfully!
  Order ID: 9876543210
  Status: NEW

Log file: logs/trading_bot.log
```

The order status will be **NEW** until:
- Price reaches 2000 USDT and order fills, OR
- Order is manually cancelled

### Test 5: API Error Handling

Test various error scenarios:

#### Invalid Symbol
```bash
python cli.py --symbol INVALID --side BUY --order-type MARKET --quantity 0.001
```
Expected: `Binance API Error: Status 400 - Invalid symbol`

#### Insufficient Balance
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 999999
```
Expected: `Binance API Error: Status 400 - Account has insufficient balance`

## Checking Logs

All orders are logged to `logs/trading_bot.log`:

```bash
# View the log file
cat logs/trading_bot.log

# Follow logs in real-time
tail -f logs/trading_bot.log

# Count successful orders
grep "ORDER PLACED SUCCESSFULLY" logs/trading_bot.log | wc -l

# Count failed orders
grep "ORDER FAILED" logs/trading_bot.log | wc -l
```

### Log File Structure

Each order attempt creates entries in this format:

```
TIMESTAMP | LOG_LEVEL | MODULE | MESSAGE
2024-05-01 10:30:45,123 | INFO | CLI | Initializing Binance Testnet Client...
2024-05-01 10:30:46,345 | INFO | bot.orders | ORDER REQUEST SUMMARY
...
2024-05-01 10:30:47,567 | INFO | bot.orders | ORDER PLACED SUCCESSFULLY
```

## Monitoring Testnet Positions

After placing orders, you can monitor them in the testnet:

1. Login to [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Go to **Positions** to see open positions
3. Go to **Orders** to see order history
4. Go to **Trade History** to see executed trades

## Troubleshooting

### Issue: "Missing Binance API credentials"
**Solution**: 
- Check `.env` file exists in the project root
- Verify `BINANCE_API_KEY` and `BINANCE_API_SECRET` are set
- Make sure there are no spaces in the values

### Issue: "Connection refused"
**Solution**:
- Check internet connection
- Verify testnet URL is accessible
- Check if API credentials are valid
- Make sure API key is enabled for futures trading

### Issue: "Account has insufficient balance"
**Solution**:
- Login to testnet account and check balance
- Reset testnet account if balance is too low
- Use smaller order quantities

### Issue: "Invalid symbol"
**Solution**:
- Check symbol format (e.g., BTCUSDT, ETHUSDT)
- Visit testnet trading page to see available symbols
- Symbol should be at least 6 characters

## Sample Test Outputs

### Successful Market Order Output

```
2024-05-01 10:30:45,123 | INFO | CLI | Initializing Binance Testnet Client...
2024-05-01 10:30:46,234 | INFO | bot.client | Binance Futures Testnet client initialized successfully
2024-05-01 10:30:46,345 | INFO | bot.orders | ======================================================================
2024-05-01 10:30:46,345 | INFO | bot.orders | ORDER REQUEST SUMMARY
2024-05-01 10:30:46,345 | INFO | bot.orders | Symbol:        BTCUSDT
2024-05-01 10:30:46,345 | INFO | bot.orders | Side:          BUY
2024-05-01 10:30:46,345 | INFO | bot.orders | Order Type:    MARKET
2024-05-01 10:30:46,345 | INFO | bot.orders | Quantity:      0.001
2024-05-01 10:30:47,567 | INFO | bot.orders | ORDER PLACED SUCCESSFULLY
2024-05-01 10:30:47,567 | INFO | bot.orders | Order ID:            1234567890
2024-05-01 10:30:47,567 | INFO | bot.orders | Status:              FILLED
```

## Performance Notes

- **Market Orders**: Execute immediately at best available price
- **Limit Orders**: Wait until price reaches target (or are cancelled)
- **API Response Time**: Usually 100-500ms
- **Logging Overhead**: Minimal impact on performance

## Cleanup After Testing

After testing, you can:

1. Clear old log files:
   ```bash
   rm logs/trading_bot.log
   ```

2. Cancel any open limit orders on testnet dashboard

3. Keep sample log files for reference:
   ```bash
   logs/SAMPLE_MARKET_ORDER.log
   logs/SAMPLE_LIMIT_ORDER.log
   ```

## Next Steps

- Review the [README.md](README.md) for setup and usage
- Check the [Project Structure](README.md#project-structure) section
- Explore the code in `bot/` directory
- Monitor testnet account at [Binance Futures Testnet](https://testnet.binancefuture.com)

---

**Need Help?** Check the logs in `logs/trading_bot.log` for detailed error messages and timestamps.
