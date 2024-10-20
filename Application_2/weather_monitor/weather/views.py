import requests
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from .models import DailyWeatherSummary

API_KEY = "2e3ca0fab992fb67a0d0b320d23e6e71"
METRO_CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather_data(city):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        kelvin_temp = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']
        temp_celsius = kelvin_temp - 273.15
        feels_like_celsius = feels_like_kelvin - 273.15
        main_condition = data['weather'][0]['main']
        timestamp = data['dt']
        return {
            'temp': round(temp_celsius, 2),
            'feels_like': round(feels_like_celsius, 2),
            'main_condition': main_condition,
            'timestamp': timestamp
        }
    else:
        return None

def calculate_daily_summary():
    daily_summary = {
        'average_temp': 0,
        'max_temp': float('-inf'),
        'min_temp': float('inf'),
        'dominant_condition': '',
    }

    weather_data = []
    condition_count = {}

    for city in METRO_CITIES:
        data = fetch_weather_data(city)
        if data:
            temp = data['temp']
            daily_summary['average_temp'] += temp
            daily_summary['max_temp'] = max(daily_summary['max_temp'], temp)
            daily_summary['min_temp'] = min(daily_summary['min_temp'], temp)
            weather_data.append(data)

            condition = data['main_condition']
            if condition not in condition_count:
                condition_count[condition] = 0
            condition_count[condition] += 1

    daily_summary['average_temp'] /= len(METRO_CITIES)

    daily_summary['dominant_condition'] = max(condition_count, key=condition_count.get)

    return daily_summary


def check_alerts(summary):
    temperature_threshold = 35.0  
    if summary['max_temp'] > temperature_threshold:
        return f"Temperature exceeded {temperature_threshold}°C."
    return None

def city_weather(request):
    city = request.GET.get('city', None)
    if city:
        weather_data = fetch_weather_data(city)
        
        if weather_data:
            weather_data['timestamp'] = datetime.fromtimestamp(weather_data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            return JsonResponse(weather_data)
        else:
            return JsonResponse({"error": "Failed to retrieve weather data"}, status=400)
    
    return JsonResponse({"error": "City not found"}, status=400)

def weather_summary(request):
    cities = METRO_CITIES  
    today_summary = calculate_daily_summary()
    alert = check_alerts(today_summary)
    
    DailyWeatherSummary.objects.create(
        date=datetime.now().date(),
        average_temp=today_summary['average_temp'],
        max_temp=today_summary['max_temp'],
        min_temp=today_summary['min_temp'],
        dominant_condition=today_summary['dominant_condition']
    )

    summaries = DailyWeatherSummary.objects.all()

    return render(request, 'weather_summary.html', {
        'summaries': summaries,
        'alert': alert,
        'cities': cities
    })
