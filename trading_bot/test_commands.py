#!/usr/bin/env python3
"""
Example script demonstrating how to run trading bot commands.

This script shows how to place:
1. Market orders (BUY/SELL)
2. Limit orders (BUY/SELL)

To run this script:
    python test_commands.py

Make sure you have:
    - Configured .env with BINANCE_API_KEY and BINANCE_API_SECRET
    - Installed dependencies: pip install -r requirements.txt
"""

import subprocess
import sys

def run_command(description, command):
    """Helper to run and display command."""
    print("\n" + "="*70)
    print(f"Test: {description}")
    print("="*70)
    print(f"Command: {' '.join(command)}")
    print("-"*70)
    
    try:
        result = subprocess.run(command, capture_output=False, text=True)
        if result.returncode == 0:
            print(f"✓ {description} completed")
        else:
            print(f"✗ {description} failed with return code {result.returncode}")
    except Exception as e:
        print(f"✗ Error running command: {e}")
    
    print("="*70)

def main():
    """Run example trading commands."""
    print("\n" + "="*70)
    print("BINANCE FUTURES TESTNET TRADING BOT - EXAMPLES")
    print("="*70)
    print("\nThis script demonstrates how to use the trading bot.")
    print("Make sure to configure your .env file first!\n")

    # Example 1: Market Buy Order
    print("\n>>> Example 1: Place a MARKET BUY order")
    print("This will buy 0.001 BTC at current market price.")
    print("\nTo execute, uncomment the code below and run:")
    print("python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001")
    
    # Example 2: Market Sell Order
    print("\n\n>>> Example 2: Place a MARKET SELL order")
    print("This will sell 0.001 BTC at current market price.")
    print("\nTo execute, run:")
    print("python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001")
    
    # Example 3: Limit Buy Order
    print("\n\n>>> Example 3: Place a LIMIT BUY order")
    print("This will place a buy order for 0.001 BTC at price 30000 USDT.")
    print("\nTo execute, run:")
    print("python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 30000")
    
    # Example 4: Limit Sell Order
    print("\n\n>>> Example 4: Place a LIMIT SELL order")
    print("This will place a sell order for 0.001 ETH at price 2000 USDT.")
    print("\nTo execute, run:")
    print("python cli.py --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 2000")
    
    print("\n" + "="*70)
    print("COMMAND LINE HELP")
    print("="*70)
    print("\nFor more information about command-line arguments, run:")
    print("python cli.py --help")
    
    print("\n" + "="*70)
    print("LOG FILES")
    print("="*70)
    print("All orders and errors are logged to: logs/trading_bot.log")
    print("\nCheck the log file after running commands to see detailed:")
    print("  - Request parameters")
    print("  - API responses")
    print("  - Error messages (if any)")
    print("  - Timestamps for all actions")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
