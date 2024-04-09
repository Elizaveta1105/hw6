import logging
import random

import psycopg2

from psycopg2 import DatabaseError
from faker import Faker
from random import randint, choice

fake = Faker()

conn = psycopg2.connect(host='localhost', database="postgres", user="postgres", password="password")
curr = conn.cursor()

for _ in range(1, 4):
    curr.execute('INSERT INTO groups (name) VALUES (%s)', (fake.word(),))

for _ in range(1, 4):
    curr.execute('INSERT INTO teachers (fullname) VALUES (%s)', (fake.name(),))


for _ in range(1, 7):
    curr.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)', (fake.bs(), choice([1, 2, 3]), ))


for _ in range(1, 45):
    curr.execute('INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id',
                 (fake.name(), choice([1, 2, 3]),))
    student_id = curr.fetchone()[0]

    for _ in range(1, 4):
        curr.execute('INSERT INTO notes (student_id, subject_id, note, note_date) VALUES (%s, %s, %s, %s)',
                     (student_id, choice([1, 2, 3]), randint(0, 100), fake.date_this_decade(),))

try:
    conn.commit()
except DatabaseError as err:
    logging.error(err)
    conn.rollback()
finally:
    curr.close()
    conn.close()
