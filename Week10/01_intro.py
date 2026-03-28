# PostgreSQL Functions & Stored Procedures
#
# A Function is a named block of SQL/PL/pgSQL code that:
#   - accepts parameters
#   - performs computation
#   - RETURNS a value (a scalar, a row, or an entire table)
#   - is called with SELECT
#
# A Stored Procedure is similar, but:
#   - designed for performing ACTIONS (inserts, updates, deletes)
#   - does NOT return a value
#   - is called with CALL
#
# PL/pgSQL is PostgreSQL's procedural language that adds
# variables, loops, conditionals, and exception handling to plain SQL

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)


# SQL command to create a new table called "students"
# Each column has a name and a data type:
#   id      - SERIAL means auto-incrementing integer (1, 2, 3, ...)
#   PRIMARY KEY means this column uniquely identifies each row
#   name    - VARCHAR(255) is a string up to 255 characters
#   major   - VARCHAR(10) is a string up to 10 characters
#   gpa     - NUMERIC stores decimal numbers (e.g. 3.75)
#   year    - INTEGER stores whole numbers
create_table = """CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            major VARCHAR(10),
            gpa NUMERIC,
            year INTEGER
        )"""

# --- Creating Functions ---

# This function takes no parameters and returns ALL rows from the students table
# RETURNS TABLE (...) defines the shape of the returned rows
# $$ ... $$ is the function body delimiter (alternative to single quotes)
# RETURN QUERY sends the result of a SELECT back to the caller
create_func_select_all = """
    CREATE OR REPLACE FUNCTION select_all()
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students;
    END;
    $$
    LANGUAGE plpgsql;
"""

# This function takes a parameter (letter) and filters students
# whose name starts with that letter
# LEFT(string, n) extracts the first n characters of a string
create_func_filter_by_first_letter = """
    CREATE OR REPLACE FUNCTION filter_by_first_letter(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students WHERE LEFT(students.name, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""

# --- Creating a Stored Procedure ---

# Unlike functions, procedures use PROCEDURE instead of FUNCTION
# and have no RETURNS clause - they perform an action and that's it
create_proc_delete_by_name = """
    CREATE OR REPLACE PROCEDURE delete_by_name(name_to_delete VARCHAR)
    AS
    $$
    BEGIN
        DELETE FROM students WHERE students.name = name_to_delete;
    END;
    $$
    LANGUAGE plpgsql;
"""

# --- Python helper functions ---

# Executes any SQL command (used to CREATE functions/procedures)
# We need commit() because CREATE statements modify the database schema
def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Way 1: Call a function using a regular SELECT statement
# Functions that RETURN TABLE can be used just like a regular table in SELECT
def call_select_all():
    command = "SELECT * FROM select_all()"
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Way 2: Call a function using psycopg2's callproc() shortcut
# callproc(name) is equivalent to: SELECT * FROM name()
def call_function(function_name):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Way 2 with arguments: callproc(name, args) passes parameters to the function
# args must be a tuple - ('R',) passes the letter 'R' as the first parameter
def call_function_w_args(function_name, args):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name, args)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Calling a PROCEDURE is different from calling a function:
# use the CALL keyword, not SELECT
# Procedures modify data, so we need conn.commit() afterwards
def call_delete_by_name(name):
    command = "CALL delete_by_name(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# --- Usage ---
# Step 1: Create the function/procedure (only needed once)
# Step 2: Call it as many times as you want

# execute_query(create_table)

# execute_query(create_func_select_all)
# print(call_select_all())
# print(call_function('select_all'))

# execute_query(create_func_filter_by_first_letter)
# print(call_function_w_args('filter_by_first_letter', ('R',)))

# execute_query(create_proc_delete_by_name)
# call_delete_by_name('Ramazan')

conn.close()