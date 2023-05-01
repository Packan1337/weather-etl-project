import psycopg2
from sqlalchemy import create_engine


# Create a PostgreSQL engine for use with SQLAlchemy.
def create_postgresql_engine(database, user, password, host, port):
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine


# Save a Pandas DataFrame to a PostgreSQL table.
def save_dataframe_to_postgresql(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
