import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt


# Fetch weather data for a specific location using the OpenWeatherMap API.
# The API key and location are specified as function arguments.
# The API key is stored in a .env file, which is not included in the repository.
# The location is specified as a string, e.g. "Stockholm".
# The API returns a JSON response, which is converted to a Python dictionary.
def fetch_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    payload = {
        "appid": api_key,
        "q": location,
        "units": "metric"
    }
    response = requests.get(base_url, params=payload)

    # Check if the request was successful.
    # If the request was successful, the response code will be 200.
    # If the request failed, the response code will be 404.
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.text}")


# Save raw and converted weather data as a JSON file in the specified folder.
# The default folder is 'raw', but you can also specify 'harmonized' or 'converted'.
def save_data(data, filename, folder='raw', data_type='raw'):
    folder_path = os.path.join(folder, data_type)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# Parse and harmonize raw weather data into a format suitable for Pandas and matplotlib.
# The raw weather data is a nested dictionary, which is difficult to work with.
# The harmonized weather data is a flat dictionary, which is easier to work with.
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


# Convert harmonized weather data to a Pandas DataFrame.
# This is useful for plotting the data with matplotlib.
# The DataFrame is also useful for saving the data to a PostgreSQL database.
def harmonized_data_to_dataframe(harmonized_data):
    data = [harmonized_data]
    columns = ["location", "weather", "temperature",
               "humidity", "wind_speed", "timestamp"]
    df = pd.DataFrame(data, columns=columns)

    return df


# Plot temperature, humidity, and wind speed from the weather DataFrame.
# The plot is useful for comparing weather data from different locations.
# The plot is saved as a PNG file in the 'plots' folder.
def plot_weather_data(df):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Location')
    ax1.set_ylabel('Temperature (°C)', color='tab:red')
    ax1.bar(df['location'], df['temperature'], color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Humidity (%)', color='tab:blue')
    ax2.bar(df['location'], df['humidity'], color='tab:blue', alpha=0.5)
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    ax3 = ax1.twinx()
    ax3.set_ylabel('Wind Speed (m/s)', color='tab:green')
    ax3.bar(df['location'], df['wind_speed'], color='tab:green', alpha=0.3)
    ax3.tick_params(axis='y', labelcolor='tab:green')
    ax3.spines['right'].set_position(('outward', 60))

    fig.tight_layout()
    plt.show()
