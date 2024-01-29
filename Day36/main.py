import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "8acad88011e94b2192e98dc991b45bd2"
STOCK_API_KEY = "FD1MWITA124AHQUF"

account_sid = os.environ["ACd514914244a9072d2184d04c875562cd"]
auth_token = os.environ["65ea19c53faa0a71f66e7b7a6fd35bae"]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference
# between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
yesterday_closing_price = stock_data_list[0]["4. close"]
the_day_before_yesterday_price = stock_data_list[1]["4. close"]
difference = float(yesterday_closing_price) - float(the_day_before_yesterday_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round(difference / float(the_day_before_yesterday_price) * 100)

# actually fetch the first 3 articles for the COMPANY_NAME.
news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apikey": NEWS_API_KEY
    }
response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = response.json()
news_list = news_data["articles"]
first_three_article = news_list[:3]


# Send a separate message with each article's title and description to your phone number.
message_list = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
                for article in first_three_article]

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
client = Client(account_sid, auth_token)

if abs(diff_percent) > 3:
    for m in message_list:
        message = client.messages.create(
            from_="+12295959260",
            body=m,
            to="+989385356909"
            )
        print(message.status)
