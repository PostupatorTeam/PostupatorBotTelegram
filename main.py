import logging

import psycopg2

from config import config


def initialize_database():
    connection = psycopg2.connect(database="postgres", user='postgres', password='adhog', host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'postupatordb'")

    if not cursor.fetchone():
        cursor.execute('CREATE DATABASE python_db')
        
    connection.commit()
    connection.close()

    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog', host='127.0.0.1', port='5432')

    connection.cursor().execute("""CREATE TABLE IF NOT EXIST main_table(
                                userid TEXT,
                                name TEXT,
                                surname TEXT,
                                lastname TEXT,
                                university_name TEXT,
                                notifications BOOLEAN)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXIST spbu_table(
                                userid TEXT,
                                educational_form TEXT,
                                pay_form TEXT,
                                program TEXT,
                                place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXIST ranepa_table(
                                    userid TEXT,
                                    departament TEXT,
                                    approval TEXT,
                                    form TEXT,
                                    program TEXT,
                                    place INTEGER)""")
    connection.commit()

    connection.cursor().execute("""CREATE TABLE IF NOT EXIST etu_table(
                                    userid TEXT,
                                    form TEXT,
                                    program TEXT,
                                    place INTEGER)""")
    connection.commit()

    connection.close()


logging.basicConfig(filename=config.logs_path, format='%(levelname)s - %(message)s')
