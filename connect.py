import psycopg2
from contextlib import contextmanager


@contextmanager
def connect_to_db():
    try:
        conn = psycopg2.connect(host='localhost', database="postgres", user="postgres", password="password")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f'Failed with {err}')
