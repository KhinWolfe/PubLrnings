import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = ""
news_api_key = ""

twilio_code = ""
twilio_num = ""
account_sid = ""
auth_token = ""

stk_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": api_key
}
response = requests.get(url=STOCK_ENDPOINT, params=stk_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [values for (day, values) in data.items()]
yesterday_data = float(data_list[0]["4. close"])
dayb4yes_data = float(data_list[1]["4. close"])
diff = abs(yesterday_data - dayb4yes_data)
diff_percent = (diff / yesterday_data) * 100
if diff_percent > 0:
    news_params = {
        "apiKey": news_api_key,
        "qinTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    top_articles = articles[:3]

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          top_articles]
    print(formatted_articles)

    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_="",
            to=""
        )

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
