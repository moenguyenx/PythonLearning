import requests
from twilio.rest import Client

API_KEY = "SP8CJYU6E4SQEK11"
NEWS_API_KEY = "fc088d1b5f9d4e028f572798f40e1f7f"
account_sid = "ACeaef477590ca1642c6f3097bb9dff18a"
auth_token = "7b5436115dc018ef246076f1043bd62d"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
percentage = round((difference / float(yesterday_closing_price)) * 100, 2)

up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

if abs(percentage) >= 2:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(f"{NEWS_ENDPOINT}", params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]  # Slicing to get top 3 articles only
    formatted_articles = [f"{STOCK_NAME}: {up_down}{abs(percentage)}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
                          for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16203839913",
            to="+84941073606"
        )
else:
    print("vailon luon")
