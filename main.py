import os
api_key = os.environ.get("OMW_API_KEY")

#"lat": 40.7632288,
#"lon": 29.9262644,
#"country": "TR"

import requests
from twilio.rest import Client
import smtplib 

account_sid = os.environ.get("KEY_SID")
auth_token = os.environ.get("AUTH_TOKEN")




response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=40.7632288&lon=29.9262644&appid=487e93edf0d9e99a2b96f95c4b416536")
response.raise_for_status()
data = response.json()

weather_data = data["list"][0]["weather"][0]["id"]
#sıfırdan başilyarak 0 9:00 12:00 arasına bakmak üzere.

will_rain = False

for x in range(4):
    waether_data = data["list"][x]["weather"][0]["id"]
    if weather_data < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="it will rain. Take your umbrella.",
                     from_='+12546154628',
                     to='+905332088834'
                 )
        print(message.sid)
        
        if will_rain:
            break
if not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="it seems not to rain buddy.You dont need an umbrella.",
                     from_='+12546154628',
                     to='+905332088834'
                 )
    print(message.sid)





   



