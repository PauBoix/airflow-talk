from dis import dis
import yfinance as yf
import pendulum
import sys

def get_bitcoin_price(data_interval_start, data_interval_end):
    # print(data_interval_start)
    # print(data_interval_end)
    data = yf.download(tickers='BTC-USD', start=data_interval_start, end=data_interval_end, interval = '1m')
    print(data)

if __name__ == "__main__":
    args = sys.argv[1:]
    dis_date = pendulum.parse(args[0])
    die_date = pendulum.parse(args[1])
    get_bitcoin_price(dis_date, die_date)