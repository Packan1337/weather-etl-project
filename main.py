from weather_api import fetch_weather_data
from data_storage import save_data
from data_processing import harmonize_weather_data
from data_conversion import harmonized_data_to_dataframe, pd
from data_visualization import plot_weather_data

API_KEY = "f287254d7f65d11a9be865eeb88e798f"
LOCATIONS = ["Stockholm", "Gothenburg", "Malmo", "Uppsala", "Vasteras"]

def main():
    all_weather_data = []

    for location in LOCATIONS:
        raw_weather_data = fetch_weather_data(API_KEY, location)
        save_data(raw_weather_data, f"{location}_weather.json", data_type='raw')

        harmonized_data = harmonize_weather_data(raw_weather_data)
        save_data(harmonized_data, f"{location}_harmonized_weather.json", data_type='harmonized')

        weather_dataframe = harmonized_data_to_dataframe(harmonized_data)
        all_weather_data.append(weather_dataframe)

    combined_weather_data = pd.concat(all_weather_data, ignore_index=True)
    plot_weather_data(combined_weather_data)
if __name__ == "__main__":
    main()