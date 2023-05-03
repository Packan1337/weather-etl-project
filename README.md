# 🌦️ Weather Data Analysis Pipeline *(ETL)*
### 👥 Group Members
- Aria Kalantari *(elite programmer, no errors ever)*

### 📚 Project Overview
The Weather Data Analysis Pipeline is a Python-based project that retrieves, processes, and visualizes weather data from multiple cities using the OpenWeatherMap API. The pipeline is comprised of several steps, including data extraction, transformation, loading into a PostgreSQL database, and visualization using matplotlib.

The goal of this project is to enable users to analyze and visualize weather data effectively, providing insights into temperature, humidity, and wind speed trends across various locations.

### 📂 Project Structure
The project is organized into several modules:

- main.py: The main script that orchestrates the execution of the ETL pipeline and visualization.
- data_etl_process.py: Contains functions for data extraction, transformation, and visualization.
- database_converter.py: Handles the connection to the PostgreSQL database and saving the data to the database.

### 🌟 Features
- Fetches weather data from multiple cities using the OpenWeatherMap API.
- Processes and harmonizes raw weather data for better analysis and visualization.
- Stores the harmonized data in a PostgreSQL database.
- Visualizes weather data (temperature, humidity, and wind speed) using matplotlib.
<br>

# 💻 Installation Guide

This document provides instructions on how to install the required packages for the Weather ETL Pipeline project.

### 🔧 Prerequisites

Make sure you have Python 3.6 or higher installed on your system. You can verify the installed version by running the following command in your terminal:

```bash
python --version
```

### 📦 Install Required Packages

(It is recommended to set up a virtual environment before installing any packages).
To install the required packages, open a terminal, navigate to the project directory, and run the following command:

```bash
pip install -r requirements.txt
```

This command will install the packages listed in the requirements.txt file.

### 🌐 Set Up Environments Variables

1. Create a .env file in the project directory.
2. Add your OpenWeatherMap API key and PostgreSQL connection details to the .env file. Use the following format:

```py
OPENWEATHER_API_KEY=your_api_key
POSTGRES_DATABASE=your_database_name
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=your_postgres_host
POSTGRES_PORT=your_postgres_port
```

Replace the placeholders with your actual API key and PostgreSQL connection details.

### 🚀 Run the Project

With the required packages installed and the environment variables set up, you are ready to run the project. In the terminal, navigate to the project directory and run:

```bash
python main.py
```

This will execute the Weather ETL Pipeline.
