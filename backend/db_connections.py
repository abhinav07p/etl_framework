from sqlalchemy import create_engine
import urllib
from sqlalchemy import create_engine, text

# PostgreSQL connection
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "Ranchi0651"
POSTGRES_DB = "etl_demo"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"

postgres_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
postgres_engine = create_engine(postgres_url)


# SQL Server connection
#SQLSERVER_USER = "sa"
#SQLSERVER_PASSWORD = "your_password"
SQLSERVER_DB = "etl_demo"
SQLSERVER_HOST = "localhost"
SQLSERVER_PORT = "1433"

# Use pyodbc + driver
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=etl_demo;"
    "Trusted_Connection=yes;"  
    "Encrypt=no;" 
)

sqlserver_url = f"mssql+pyodbc:///?odbc_connect={params}"
sqlserver_engine = create_engine(sqlserver_url)


# Quick test
if __name__ == "__main__":
    with postgres_engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("✅ Connected to PostgreSQL:", result.fetchone())

    with sqlserver_engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION;"))
        print("✅ Connected to SQL Server:", result.fetchone())
