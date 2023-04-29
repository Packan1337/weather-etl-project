import pandas as pd

# Convert harmonized weather data to a Pandas DataFrame.
def harmonized_data_to_dataframe(harmonized_data):
    data = [harmonized_data]
    columns = ["location", "weather", "temperature", "humidity", "wind_speed", "timestamp"]
    df = pd.DataFrame(data, columns=columns)

    return df
