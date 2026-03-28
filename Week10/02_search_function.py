# Search by pattern using ILIKE
#
# ILIKE is case-insensitive LIKE
# The || operator concatenates strings in SQL

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

create_func_search = """
    CREATE OR REPLACE FUNCTION search_students(pattern VARCHAR)
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students
        WHERE students.name ILIKE '%' || pattern || '%'
           OR students.major ILIKE '%' || pattern || '%';
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

def search(pattern):
    command = "SELECT * FROM search_students(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (pattern,))
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# execute_query(create_func_search)
# print(search('ra'))     # finds "Raimbek", "Ramazan", etc. (case-insensitive)
# print(search('IS'))     # finds students with major "IS"

conn.close()