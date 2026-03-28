# Transactions
#\
# A transaction is a group of SQL operations that are treated as one unit
# Either ALL of them succeed (COMMIT), or NONE of them take effect (ROLLBACK)
#
# Why this matters: imagine transferring money between bank accounts
# You need to subtract from one AND add to the other
# If the program crashes between the two steps, you'd lose money!
# Transactions guarantee both happen or neither happens
#
# By default, psycopg2 wraps every operation in a transaction
# conn.commit()    saves all changes since the last commit
# conn.rollback()  discards all changes since the last commit

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

# Example: transfer between two students' GPA
def safe_transfer_gpa(from_id, to_id, amount):
    try:
        with conn.cursor() as cur:
            # Both operations are part of the same transaction
            cur.execute("UPDATE students SET gpa = gpa - %s WHERE id = %s", (amount, from_id))
            cur.execute("UPDATE students SET gpa = gpa + %s WHERE id = %s", (amount, to_id))

            # If both succeed, commit
            conn.commit()
            print("Transfer successful")

    except (psycopg2.DatabaseError, Exception) as error:
        # If anything goes wrong, rollback - undo ALL changes
        conn.rollback()
        print(f"Transfer failed, rolled back: {error}")

# Example: what happens when we rollback
def rollback_demo():
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students(name, major, gpa, year) VALUES(%s, %s, %s, %s)",
                        ("Temporary Student", "CS", 3.0, 1))

            # Oops, we changed our mind - rollback discards the insert
            conn.rollback()
            print("Rolled back - the student was NOT inserted")

            # Verify
            cur.execute("SELECT * FROM students WHERE name = 'Temporary Student'")
            print("Found:", cur.fetchall())  # should be empty

    except (psycopg2.DatabaseError, Exception) as error:
        conn.rollback()
        print(error)

# safe_transfer_gpa(1, 2, 0.5)
# rollback_demo()

conn.close()