import logging

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import config
import psycopg2
from middle_module import middle_module
from telegram_module.telegram_module import start


def main():
    start()


def initialize_database():
    connection = psycopg2.connect(database="postgres", user='postgres', password='adhog', host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'postupatordb'")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE

    if not cursor.fetchone():
        cursor.execute('CREATE DATABASE postupatordb')

    connection.commit()
    connection.close()

    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog', host='127.0.0.1', port='5432')

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS main_table(
                                userid TEXT,
                                name TEXT,
                                surname TEXT,
                                lastname TEXT,
                                university_name TEXT,
                                notifications BOOLEAN)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS spbu_table(
                                userid TEXT,
                                educational_form TEXT,
                                pay_form TEXT,
                                program TEXT,
                                place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS ranepa_table(
                                    userid TEXT,
                                    departament TEXT,
                                    approval TEXT,
                                    form TEXT,
                                    program TEXT,
                                    place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXISTS etu_table(
                                    userid TEXT,
                                    form TEXT,
                                    program TEXT,
                                    place INTEGER)""")
    connection.commit()
    connection.close()


if __name__ == '__main__':
    logging.basicConfig(filename=config.logs_path, format='%(levelname)s - %(message)s')
    initialize_database()
    middle_module.notify()
    main()
