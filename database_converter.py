import psycopg2
from sqlalchemy import create_engine


# Create a PostgreSQL engine for use with SQLAlchemy.
# The engine is used to connect to the PostgreSQL database and save a Pandas DataFrame to a PostgreSQL table.
def create_postgresql_engine(database, user, password, host, port):
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine


# Save a Pandas DataFrame to a PostgreSQL table.
# The PostgreSQL table is created if it does not already exist.
# The PostgreSQL table is truncated before the new data is inserted.
def save_dataframe_to_postgresql(df, table_name, engine):
    with engine.connect() as connection:
        connection.execute(
            f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE")

    df.to_sql(table_name, engine, if_exists='append', index=False)
