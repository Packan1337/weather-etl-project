# Weather Data Analysis Pipeline
## Group Members
- Aria Kalantari

## Project Overview
The Weather Data Analysis Pipeline is a Python-based project that retrieves, processes, and visualizes weather data from multiple cities using the OpenWeatherMap API. The pipeline is comprised of several steps, including data extraction, transformation, loading into a PostgreSQL database, and visualization using matplotlib.

The goal of this project is to enable users to analyze and visualize weather data effectively, providing insights into temperature, humidity, and wind speed trends across various locations.

## Project Structure
The project is organized into several modules:

- main.py: The main script that orchestrates the execution of the ETL pipeline and visualization.
- data_etl_process.py: Contains functions for data extraction, transformation, and visualization.
- database_converter.py: Handles the connection to the PostgreSQL database and saving the data to the database.

## Features
- Fetches weather data from multiple cities using the OpenWeatherMap API.
- Processes and harmonizes raw weather data for better analysis and visualization.
- Stores the harmonized data in a PostgreSQL database.
- Visualizes weather data (temperature, humidity, and wind speed) using matplotlib.
