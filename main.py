from dotenv import load_dotenv
from data_etl_process import *
from database_converter import *

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
LOCATIONS = ["Stockholm", "Gothenburg", "Malmo",
             "Uppsala", "Vasteras", "Bollnas", "Kiruna"]

database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")


API_KEY = "f287254d7f65d11a9be865eeb88e798f"
database = "WeatherDB"
user = "packan"
password = "Ariadencoole1"
host = "localhost"
port = "5432"


def main():
    all_weather_data = []

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

    # Create the PostgreSQL engine
    engine = create_postgresql_engine(database, user, password, host, port)

    # Save the DataFrame to a PostgreSQL table
    save_dataframe_to_postgresql(combined_weather_data, "weather_data", engine)


if __name__ == "__main__":
    main()
