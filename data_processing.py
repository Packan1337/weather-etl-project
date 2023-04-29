# Parse and harmonize raw weather data into a format suitable for Pandas and matplotlib.
def harmonize_weather_data(raw_data):
    harmonized_data = {
        "location": raw_data["name"],
        "weather": raw_data["weather"][0]["description"],
        "temperature": raw_data["main"]["temp"],
        "humidity": raw_data["main"]["humidity"],
        "wind_speed": raw_data["wind"]["speed"],
        "timestamp": raw_data["dt"]
    }

    return harmonized_data
