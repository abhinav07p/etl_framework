import yaml
import urllib.parse
from sqlalchemy import create_engine, text


# 1. Load database config
with open("backend/configs/db_config.yaml", "r") as file:
    config = yaml.safe_load(file)

postgres_url = (
    f"postgresql+psycopg2://{config['sources'][0]['user']}:{config['sources'][0]['password']}@{config['sources'][0]['host']}:{config['sources'][0]['port']}/{config['sources'][0]['dbname']}"
)

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=etl_demo;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=Yes;"
)

# 2. Create engine connections
pg_engine = create_engine(postgres_url)
mssql_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 3. Extract data from PostgreSQL
with pg_engine.connect() as pg_conn:
    result = pg_conn.execute(text("SELECT id, name, email, age FROM users"))
    rows = result.fetchall()

print(f"📥 Extracted {len(rows)} rows from PostgreSQL.")

# 4. Load data into SQL Server
with mssql_engine.begin() as mssql_conn:  # begin() = transaction
    for row in rows:
        mssql_conn.execute(
            text("INSERT INTO users (name, email, age) VALUES (:name, :email, :age)"),
            {"name": row.name, "email": row.email, "age": row.age}
        )

print("✅ Data successfully loaded into SQL Server!")
