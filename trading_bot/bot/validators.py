"""Input validation module for trading bot."""

def validate_side(side: str) -> str:
    """
    Validates and returns the order side (BUY or SELL).
    
    Args:
        side: The order side as a string (case-insensitive)
        
    Returns:
        str: Uppercase side (BUY or SELL)
        
    Raises:
        ValueError: If side is not BUY or SELL
    """
    if not side or not isinstance(side, str):
        raise ValueError("Side must be a non-empty string.")
    
    side_upper = side.upper()
    if side_upper not in ['BUY', 'SELL']:
        raise ValueError("Invalid side. Must be 'BUY' or 'SELL'.")
    return side_upper

def validate_order_type(order_type: str) -> str:
    """
    Validates and returns the order type (MARKET or LIMIT).
    
    Args:
        order_type: The order type as a string (case-insensitive)
        
    Returns:
        str: Uppercase order type (MARKET or LIMIT)
        
    Raises:
        ValueError: If order_type is not MARKET or LIMIT
    """
    if not order_type or not isinstance(order_type, str):
        raise ValueError("Order type must be a non-empty string.")
    
    type_upper = order_type.upper()
    if type_upper not in ['MARKET', 'LIMIT']:
        raise ValueError("Invalid order type. Must be 'MARKET' or 'LIMIT'.")
    return type_upper

def validate_symbol(symbol: str) -> str:
    """
    Validates trading symbol format.
    
    Args:
        symbol: The trading pair symbol (e.g., BTCUSDT, ETHUSDT)
        
    Returns:
        str: Uppercase symbol
        
    Raises:
        ValueError: If symbol format is invalid
    """
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    
    symbol_upper = symbol.upper()
    # Basic check: symbol should be at least 6 chars (like USDT pairs are typically 6-10 chars)
    if len(symbol_upper) < 6:
        raise ValueError(f"Invalid symbol '{symbol}'. Expected format like 'BTCUSDT' or 'ETHUSDT'.")
    
    return symbol_upper

def validate_quantity(quantity: float) -> float:
    """
    Validates order quantity is positive.
    
    Args:
        quantity: The order quantity (must be positive number)
        
    Returns:
        float: The validated quantity
        
    Raises:
        ValueError: If quantity is not a positive number
    """
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
        return qty
    except (ValueError, TypeError):
        raise ValueError(f"Invalid quantity '{quantity}'. Must be a positive number.")

def validate_price(price: float) -> float:
    """
    Validates limit order price is positive.
    
    Args:
        price: The limit price (must be positive number or None for market orders)
        
    Returns:
        float: The validated price, or None if input is None
        
    Raises:
        ValueError: If price is not a positive number (when provided)
    """
    if price is None:
        return None
    
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than 0.")
        return p
    except (ValueError, TypeError):
        raise ValueError(f"Invalid price '{price}'. Must be a positive number.")
