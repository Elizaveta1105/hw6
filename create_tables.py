import logging

from connect import connect_to_db
from psycopg2 import DatabaseError


def create_table(conn, sql_expression):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as err:
        print(err)
        conn.rollback()


if __name__ == '__main__':
    # sql_create_table = """
    # CREATE TABLE IF NOT EXISTS notes(
    #     id serial PRIMARY KEY,
    #     student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    #     subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
    #     note INTEGER CHECK(note >= 0 AND note <=100),
    #     note_date DATE NOT NULL
    # )"""
    # sql_create_table = """
    #     CREATE TABLE groups (
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(50) NOT NULL
    #     )"""

    # sql_create_table = """
    #     CREATE TABLE students (
    #         id SERIAL PRIMARY KEY,
    #         fullname VARCHAR(150) NOT NULL,
    #         group_id INTEGER REFERENCES groups(id)
  	#             on delete cascade
    #     )"""
#
#     sql_create_table = """
#     CREATE TABLE teachers (
#         id SERIAL PRIMARY KEY,
#         fullname VARCHAR(150) NOT NULL
# );"""

#     sql_create_table = """
#     CREATE TABLE subjects (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(175) NOT NULL,
#         teacher_id INTEGER  REFERENCES teachers(id)
#   	            on delete cascade
# );"""

    try:
        with connect_to_db() as conn:
            if conn is not None:
                create_table(conn, sql_create_table)
            else:
                print('Error')
    except RuntimeError as err:
        logging.error(err)
