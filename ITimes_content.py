import csv
import random
import json
import datetime
from urllib import request

# Function for a random quote
def get_random_quote(quotes_file="quotes.csv"):
    try:
        with open(quotes_file) as csvfile:
            quotes = [{"author": line[0],
                       "quote": line[1]} for line in csv.reader(csvfile, delimiter="|")]
    
    except Exception as e:
        quotes = [{"author": "Mother Teresa",
                   "quote": "I alone cannot change the world, but I can cast a stone across the water to create many ripples."}]
    
    return random.choice(quotes)

# Function for weather report with default location as Hyderabad, India
def get_weather_forecast(coordinates = {"latitude": 17.387140, "longitude":78.491684}):
    try:
        api_key = "46751297e53ffbafcdad13a74df9db1b"
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={coordinates['latitude']}&lon={coordinates['longitude']}&appid={api_key}&units=metric"
        data = json.load(request.urlopen(url))
        
        forecast = {"city": data["city"]["name"],
                    "country": data["city"]["country"],
                    "periods": list()}
        
        for period in data["list"][0:9]:
            forecast["periods"].append({"timestamp": datetime.datetime.fromtimestamp(period["dt"]),
                                        "temp": round(period["main"]["temp"]),
                                        "description": period["weather"][0]["description"].title(),
                                        "icon": f"http://openweathermap.org/img/wn/{period['weather'][0]['icon']}.png"})
        return forecast

    except Exception as e:
        print(e)

