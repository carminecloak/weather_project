from django.shortcuts import render
from django.http import HttpResponse
import requests
from pymongo import MongoClient

def fetch_and_save_weather(request):
    api_key = "f9ff48b7cb0b3613ec3c9729502cfcf7"
    lat = 44.85
    lon = 20.45

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'name' in data:
        city = data["name"]
        temperature = data["main"]["temp"]

        # Save to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["weather_db"]
        collection = db["weather_data"]

        weather_info = {
            "city": city,
            "temperature": temperature,
        }
        collection.insert_one(weather_info)

        return HttpResponse(f"Weather data for {city} saved to MongoDB.")
    else:
        return HttpResponse("Error fetching weather data.")
