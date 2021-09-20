
import requests
from twilio.rest import Client

# CONSTANTS
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = "Your AlphaVantage api key"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_KEY = "Your NewsAPI key"

account_sid = "Your Twilio account sid"
auth_token = "Your Twilio auth token"

# Parameters for stock API request
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}

# API request for stock information
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# Yesterday's close price
yesterday = stock_data_list[0]
yesterday_close = float(yesterday["4. close"])

# The day before yesterday's close price
day_before_yesterday = stock_data_list[1]
day_before_yesterday_close = float(day_before_yesterday["4. close"])

# Difference in price
price_difference = yesterday_close - day_before_yesterday_close

# Arrow emojis to be added to SMS message
arrow = None
if price_difference > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

# Percentage difference in price
percentage = round((price_difference / yesterday_close) * 100)

# If there is a 5% difference in price, the SMSes containing news articles will be sent
if abs(percentage) > 5:

    # Parameters for news API request
    news_parameters = {
        "apiKey": NEWSAPI_KEY,
        "qInTitle": COMPANY_NAME,
    }

    # API request for news information
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"]

    # First three articles
    three_articles = news_data[:3]
    print(three_articles)

    articles_list = [f"{STOCK_NAME}: {arrow}{percentage}% Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]

    # Send articles via SMS
    client = Client(account_sid, auth_token)
    for article in articles_list:
        message = client.messages.create(
            body=article,
            from_="Your Twilio virtual number",
            to="Your real number"
        )
