import psycopg2
from config import load_config

def connect(config):
    """ Подключение к серверу базы данных PostgreSQL """
    try:
        # Подключение к серверу PostgreSQL
        with psycopg2.connect(**config) as conn:
            print('Подключено к серверу PostgreSQL.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)
    conn = psycopg2.connect("dbname=suppliers user=postgres host=localhost por=5433")
    