import yfinance as yf
import datetime
import time
from plyer import notification

stock_name = input("Enter the stock symbol (e.g., TATAPOWER.BO): ")

while True:
    stock = yf.Ticker(stock_name)

    try:

        info = stock.fast_info

        notification.notify(
            title=f"📈 Market Alert - {datetime.date.today()}",
            message=(
                f"{stock.info['shortName']}\n"
                f"Current Price = ₹{info['lastPrice']:.2f}\n"
                f"Day High = ₹{info['dayHigh']:.2f}\n"
                f"Day Low = ₹{info['dayLow']:.2f}"
            ),
            app_icon="icon.ico",
            timeout=5
        )

    except Exception as e:
        print(f"Error fetching data: {e}")

    time.sleep(10)
