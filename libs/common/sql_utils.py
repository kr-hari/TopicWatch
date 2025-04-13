import json
import logging
from os import environ, mkdir, path, remove
from pgvector.psycopg2 import register_vector
from psycopg2.pool import SimpleConnectionPool
from psycopg2 import OperationalError
import time
from dotenv import load_dotenv
load_dotenv()

from libs.common.utils import timer_decorator


def get_db_url():
    """
    Constructs the database URL from environment variables.
    """
    db_host = environ.get("POSTGRES_HOST", "localhost")
    db_port = environ.get("POSTGRES_PORT", "5432")
    db_name = environ.get("POSTGRES_DB", "mydatabase")
    db_user = environ.get("POSTGRES_USER", "myuser")
    db_password = environ.get("POSTGRES_PASSWORD", "mypassword")
    db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return db_url