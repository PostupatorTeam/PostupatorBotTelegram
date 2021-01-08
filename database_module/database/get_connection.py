from psycopg2 import connect
from config.config import database_name, user, password, host, port


def get_connection() -> connect:
    return connect(database=database_name, user=user, password=password, host=host, port=port)
