# Transactions - batch insert with error handling
#
# A common pattern: insert many rows, but if any one fails,
# roll back the entire batch so you don't end up with partial data

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

def insert_students_batch(students_list):
    """
    Insert a list of students as a single transaction
    If any insert fails, the entire batch is rolled back
    students_list: list of tuples (name, major, gpa, year)
    """
    command = "INSERT INTO students(name, major, gpa, year) VALUES(%s, %s, %s, %s)"
    try:
        with conn.cursor() as cur:
            for student in students_list:
                cur.execute(command, student)
            conn.commit()
            print(f"Successfully inserted {len(students_list)} students")
    except (psycopg2.DatabaseError, Exception) as error:
        conn.rollback()
        print(f"Batch insert failed, all rolled back: {error}")


good_batch = [
    ("Alice", "CS", 3.8, 2),
    ("Bob", "IS", 3.5, 3),
    ("Charlie", "DS", 4.0, 1),
]

# This batch has a problem - "INVALID_MAJOR_THAT_IS_WAY_TOO_LONG" exceeds VARCHAR(10)
bad_batch = [
    ("Diana", "CS", 3.9, 2),
    ("Eve", "INVALID_MAJOR_THAT_IS_WAY_TOO_LONG", 3.0, 1),
    ("Frank", "IS", 3.2, 4),
]

# insert_students_batch(good_batch)   # all 3 inserted
# insert_students_batch(bad_batch)    # all 3 rolled back - Diana and Frank are NOT inserted

conn.close()