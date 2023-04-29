from weather_api import fetch_weather_data
from data_storage import save_raw_data

API_KEY = "f287254d7f65d11a9be865eeb88e798f"
LOCATION = "Stockholm"

def main():
    weather_data = fetch_weather_data(API_KEY, LOCATION)
    save_raw_data(weather_data, f"{LOCATION}_weather.json")

if __name__ == "__main__":
    main()
