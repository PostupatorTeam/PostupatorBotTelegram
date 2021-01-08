from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config.config import user, password, host, port, database_name


def create_database():
    connection = connect(database="postgres", user=user, password=password, host=host, port=port)
    cursor = connection.cursor()
    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database_name}'")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {database_name}")

    connection.commit()
    connection.close()


def create_tables():
    connection = connect(database=database_name, user=user, password=password, host=host, port=port)

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS main_table(
                                                                userid TEXT, name TEXT, surname TEXT, lastname TEXT,
                                                                university_name TEXT, notifications BOOLEAN)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS spbu_table(
                                                                userid TEXT, educational_form TEXT, pay_form TEXT,
                                                                program TEXT, place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS ranepa_table(
                                                                userid TEXT, departament TEXT, approval TEXT,
                                                                form TEXT, program TEXT, place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS etu_table(
                                                                userid TEXT, form TEXT, program TEXT, place INTEGER)""")
    connection.commit()

    connection.close()
