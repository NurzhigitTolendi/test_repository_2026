# PostgreSQL Function: pagination with LIMIT and OFFSET
#
# Instead of loading all rows at once, we can fetch them in pages
# This function takes a page size (limit) and page number,
# and returns just that page of results

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

create_func_paginated = """
    CREATE OR REPLACE FUNCTION get_students_page(page_limit INTEGER, page_offset INTEGER)
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students
        ORDER BY students.id
        LIMIT page_limit
        OFFSET page_offset;
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

def get_page(limit, offset):
    command = "SELECT * FROM get_students_page(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (limit, offset))
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# execute_query(create_func_paginated)
# print("Page 1:", get_page(3, 0))   # first 3 students
# print("Page 2:", get_page(3, 3))   # next 3 students
# print("Page 3:", get_page(3, 6))   # next 3 (may be empty or partial)

conn.close()