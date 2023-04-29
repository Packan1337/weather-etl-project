import requests

# Fetch weather data for a specific location using the OpenWeatherMap API.
def fetch_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    payload = {
        "appid": api_key,
        "q": location,
        "units": "metric"
    }
    response = requests.get(base_url, params=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.text}")
