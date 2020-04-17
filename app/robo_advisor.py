# app/robo_advisor.py

import csv
import json
import os
from dotenv import load_dotenv
import requests
import datetime 

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

apikey = os.environ.get("API_KEY", "demo")

global symbol
symbol = ""
symbol = input("Please input a stock symbol(ex. MSFT): ") 
if len(symbol) < 1:
	print("Symbol seems too short. Please try again")
elif len(symbol) > 6: # 6 seems to be the max length of a ticker: https://www.quora.com/Whats-the-shortest-and-the-longest-that-a-companys-ticker-can-be-on-a-stock-market-exchange
	print("That symbol seems too long. Please try again.")
elif IndexError:
                print("Please try again, symbol not found")
                exit()


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]


latest_close = tsd[latest_day]["4. close"]
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

def line():
    print("-" * 60)

#Write to CSV

#csv_file_path = "data/prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })

# Recommendation 

calc = recent_low*1.2

if float(latest_close) < float(calc):
		rec_sum = "Buy!"
		rec_exp = "The latest close is less than 20% above the recent low." 
else:
		rec_sum = "Sell!"
		rec_exp = "The latest close is more than 20% above the recent low." 

# Results

line()
print(f"SELECTED SYMBOL: {symbol}")
line()
print("REQUESTING STOCK MARKET DATA...")
now = datetime.datetime.now()
line()
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
line()
print(f"RECOMMENDATION: {rec_sum}")
print(f"RECOMMENDATION REASON: {rec_exp}")
line()
print(f"WRITING DATA TO CSV: {csv_file_path}")
line()
print("HAPPY INVESTING!")
line()