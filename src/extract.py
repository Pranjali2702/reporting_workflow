from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    database = os.getenv('DB_NAME')

    conn_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(conn_str)

def extract_data(query_path, params=None):
    with open(query_path) as f:
        query = f.read()
    engine = get_engine()
    return pd.read_sql(query, engine, params=params)