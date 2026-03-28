# Upsert (insert or update)
#
# "Upsert" = INSERT if the record doesn't exist, UPDATE if it does
# Uses IF/ELSE inside PL/pgSQL

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

create_proc_upsert = """
    CREATE OR REPLACE PROCEDURE upsert_student(
        p_name VARCHAR,
        p_major VARCHAR,
        p_gpa NUMERIC,
        p_year INTEGER
    )
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM students WHERE name = p_name) THEN
            UPDATE students SET major = p_major, gpa = p_gpa, year = p_year
            WHERE name = p_name;
        ELSE
            INSERT INTO students(name, major, gpa, year)
            VALUES(p_name, p_major, p_gpa, p_year);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
"""

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def upsert_student(name, major, gpa, year):
    command = "CALL upsert_student(%s, %s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, major, gpa, year))
            conn.commit()
            print(f"Upserted: {name}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# execute_query(create_proc_upsert)
# upsert_student('Raimbek Gosling', 'CS', 4.5, 2)   # updates existing
# upsert_student('New Student', 'IS', 3.0, 1)        # inserts new

conn.close()