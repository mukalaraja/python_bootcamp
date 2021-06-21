import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "BZD4JOG4J69LCUI9"
NEWS_API_KEY =  "86e68733c5de4088b5f150ebc328b5ca"
stock_parmas = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": "STOCK_API_KEY",
}

response = requests.get(STOCK_ENDPOINT, params=stock_parmas)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 1:
  news_parmas = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
  }
  news_response = requests.get(NEWS_ENDPOINT, params=news_parmas)
  articles = news_response.json()["articles"]
  three_articles = articles[:3]
  print(three_articles)
 
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]