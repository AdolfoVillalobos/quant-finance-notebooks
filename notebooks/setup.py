import ccxt

import pandas as pd

from datetime import datetime


def fetch_ohlcv_with_pagination(symbol, timeframe, start_time, end_time):
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    # exchange.verbose = True  # uncomment for debugging purposes if necessary
    since = exchange.parse8601(start_time)

    all_ohlcvs = []
    while True:
        try:
            ohlcvs = exchange.fetch_ohlcv(symbol, timeframe, since)
            all_ohlcvs += ohlcvs
            if len(ohlcvs):
                print(
                    "Fetched",
                    len(ohlcvs),
                    symbol,
                    timeframe,
                    "candles from",
                    exchange.iso8601(ohlcvs[0][0]),
                )
                since = ohlcvs[-1][0] + 1
            else:
                break
        except Exception as e:
            print(type(e).__name__, str(e))
    print("Fetched", len(all_ohlcvs), symbol, timeframe, "candles in total")

    # Convert to DataFrame
    df = pd.DataFrame(
        all_ohlcvs, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    df.to_csv(f"notebooks/data/{symbol.replace('/', '_')}_{timeframe}.csv", sep=";")

    return df


if __name__ == "__main__":
    params = [
        {"symbol": "BTC/USDT", "timeframe": "5m"},
        {"symbol": "ETH/USDT", "timeframe": "5m"},
    ]
    for param in params:
        symbol = param["symbol"]
        timeframe = param["timeframe"]
        start_time = "2024-01-01T00:00:00Z"
        end_time = "2024-09-30T00:00:00Z"

        df = fetch_ohlcv_with_pagination(symbol, timeframe, start_time, end_time)
        print(df.head())
