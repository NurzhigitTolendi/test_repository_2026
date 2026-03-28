# Working with BLOB (Binary Large Object) data
#
# PostgreSQL uses the BYTEA data type to store binary data
# (images, PDFs, audio files, etc.) directly in the database
#
# This example stores and retrieves an image file

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

def create_files_table():
    command = """CREATE TABLE IF NOT EXISTS files (
                id SERIAL PRIMARY KEY,
                file_name VARCHAR(255),
                file_data BYTEA
            )"""
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

# Store a file in the database
def insert_file(file_path):
    with open(file_path, 'rb') as f:        # 'rb' = read binary
        file_data = f.read()

    file_name = file_path.split('/')[-1]    # extract just the filename

    command = "INSERT INTO files(file_name, file_data) VALUES(%s, %s)"
    with conn.cursor() as cur:
        cur.execute(command, (file_name, psycopg2.Binary(file_data)))
        conn.commit()
        print(f"Stored '{file_name}' ({len(file_data)} bytes)")

# Retrieve a file from the database and save it to disk
def retrieve_file(file_id, output_path):
    command = "SELECT file_name, file_data FROM files WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(command, (file_id,))
        row = cur.fetchone()

        if row is None:
            print("File not found")
            return

        file_name, file_data = row

        with open(output_path, 'wb') as f:  # 'wb' = write binary
            f.write(bytes(file_data))
        print(f"Retrieved '{file_name}' -> {output_path}")

# List all stored files (without the binary data)
def list_files():
    command = "SELECT id, file_name, LENGTH(file_data) AS size_bytes FROM files"
    with conn.cursor() as cur:
        cur.execute(command)
        for row in cur.fetchall():
            print(f"  id={row[0]}, name={row[1]}, size={row[2]} bytes")


# create_files_table()
# insert_file('some_image.png')
# list_files()
# retrieve_file(1, 'retrieved_image.png')

conn.close()