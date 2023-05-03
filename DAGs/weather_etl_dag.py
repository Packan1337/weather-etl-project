from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from main import run_weather_etl

# Import necessary variables from the .env file
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# OpenWeatherMap API key and locations
API_KEY = os.getenv("OPENWEATHER_API_KEY")
LOCATIONS = ["Stockholm", "Gothenburg", "Malmo", "Uppsala", "Vasteras", "Bollnas", "Kiruna"]

# PostgreSQL database credentials
database = os.getenv("POSTGRES_DATABASE")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_etl_dag',
    default_args=default_args,
    description='Weather ETL pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 5, 1),
    catchup=False,
)

def weather_etl_task():
    run_weather_etl(API_KEY, database, user, password, host, port, LOCATIONS)

weather_etl_operator = PythonOperator(
    task_id='weather_etl',
    python_callable=weather_etl_task,
    dag=dag,
)
