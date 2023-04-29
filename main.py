from weather_api import fetch_weather_data
from data_storage import save_raw_data
from data_processing import harmonize_weather_data


API_KEY = "f287254d7f65d11a9be865eeb88e798f"
LOCATION = "Stockholm"

def main():
    raw_weather_data = fetch_weather_data(API_KEY, LOCATION)
    save_raw_data(raw_weather_data, f"{LOCATION}_weather.json")

    harmonized_data = harmonize_weather_data(raw_weather_data)
    print(harmonized_data)

if __name__ == "__main__":
    main()
