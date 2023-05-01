from dotenv import load_dotenv
from data_etl_process import *
from database_converter import *

load_dotenv()

# OpenWeatherMap API key and locations
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
LOCATIONS = ["Stockholm", "Gothenburg", "Malmo",
             "Uppsala", "Vasteras", "Bollnas", "Kiruna"]

# PostgreSQL database credentials
# These credentials are stored in a .env file, which is not included in the repository
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")


# Fetch, parse, and save weather data for each location
# Plot the weather data for all locations
# Create the PostgreSQL engine
# The PostgreSQL table is created if it does not already exist
# The PostgreSQL table is truncated before the new data is inserted
# # Save the DataFrame to a PostgreSQL table
def main():
    all_weather_data = []

    # Fetch, parse, and save weather data for each location
    for location in LOCATIONS:
        raw_weather_data = fetch_weather_data(API_KEY, location)
        save_data(raw_weather_data,
                  f"{location}_weather.json", data_type='raw')
        
        harmonized_data = harmonize_weather_data(raw_weather_data)
        save_data(harmonized_data,
                  f"{location}_harmonized_weather.json", data_type='harmonized')

        weather_dataframe = harmonized_data_to_dataframe(harmonized_data)
        all_weather_data.append(weather_dataframe)

    combined_weather_data = pd.concat(all_weather_data, ignore_index=True)
    plot_weather_data(combined_weather_data)

    engine = create_postgresql_engine(database, user, password, host, port)

    save_dataframe_to_postgresql(combined_weather_data, "weather_data", engine)


if __name__ == "__main__":
    main()
