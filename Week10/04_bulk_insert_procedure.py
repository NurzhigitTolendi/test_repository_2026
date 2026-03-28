# Bulk insert with validation
#
# This procedure takes arrays of names, majors, GPAs, and years
# It loops through them, validates each entry, and inserts valid ones
# Invalid entries are collected and returned via a temp table
#
# Demonstrates: loops, IF, arrays, and validation inside PL/pgSQL

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

create_proc_bulk_insert = """
    CREATE OR REPLACE PROCEDURE bulk_insert_students(
        names VARCHAR[],
        majors VARCHAR[],
        gpas NUMERIC[],
        years INTEGER[]
    )
    AS $$
    DECLARE
        i INTEGER;
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            -- Validate: GPA must be between 0 and 5, year must be positive
            IF gpas[i] >= 0 AND gpas[i] <= 4 AND years[i] > 0 THEN
                INSERT INTO students(name, major, gpa, year)
                VALUES(names[i], majors[i], gpas[i], years[i]);
            ELSE
                RAISE NOTICE 'Skipped invalid entry: % (gpa=%, year=%)', names[i], gpas[i], years[i];
            END IF;
        END LOOP;
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

def bulk_insert(names, majors, gpas, years):
    command = "CALL bulk_insert_students(%s, %s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (names, majors, gpas, years))
            conn.commit()
            print(f"Bulk insert done ({len(names)} entries processed)")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# execute_query(create_proc_bulk_insert)

# Some valid, some invalid entries:
# names = ["Alice", "Bob", "Charlie"]
# majors = ["CS", "IS", "DS"]
# gpas = [3.8, 6.0, 4.0]       # Bob's GPA of 6.0 is invalid (> 4)
# years = [2, 3, -1]            # Charlie's year of -1 is invalid
# bulk_insert(names, majors, gpas, years)  # only Alice is inserted

conn.close()