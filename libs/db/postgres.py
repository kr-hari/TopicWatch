from sqlmodel import SQLModel, create_engine, Session
import os

from libs.common.sql_utils import get_db_url

# Database connection details
DB_URL = get_db_url()

# Create the engine (connects to Postgres)
engine = create_engine(
    DB_URL,
    echo=True  # Set to False to turn off SQL logs
)

# Function to create all tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a session for querying
def get_session():
    return Session(engine)