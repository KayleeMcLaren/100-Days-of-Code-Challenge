
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("your_api_key")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("your_auth_token")

parameters = {
    "lat": "your latitude",
    "lon": "your longitude",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
sliced_data = data["hourly"][:12]

will_rain = False

for hour in sliced_data:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="your virtual phone number",
        to="your real number"
    )
    print(message.status)
    
