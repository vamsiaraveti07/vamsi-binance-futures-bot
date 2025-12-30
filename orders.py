from logger import log_info, log_error

def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        log_info(f"MARKET | {symbol} | {side} | qty={quantity}")
        return order
    except Exception as e:
        log_error(f"MARKET FAILED | {e}")
        return None


def place_limit_order(client, symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        log_info(f"LIMIT | {symbol} | {side} | qty={quantity} | price={price}")
        return order
    except Exception as e:
        log_error(f"LIMIT FAILED | {e}")
        return None
    def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            log_info(
                f"STOP-LIMIT | {symbol} | {side} | qty={quantity} | "
                f"stop={stop_price} | limit={limit_price}"
            )
            return order
        except Exception as e:
            log_error(f"STOP-LIMIT FAILED | {e}")
            return None

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=limit_price,
            stopPrice=stop_price,
            timeInForce="GTC"
        )
        log_info(
            f"STOP-LIMIT | {symbol} | {side} | "
            f"qty={quantity} | stop={stop_price} | limit={limit_price}"
        )
        return order
    except Exception as e:
        log_error(f"STOP-LIMIT FAILED | {e}")
        return None


