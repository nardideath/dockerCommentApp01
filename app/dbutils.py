import time
import os
import psycopg2


def wait_for_db():
    db_host = os.getenv("DB_HOST", "db")
    db_name = os.getenv("DB_NAME", "testdb")
    db_user = os.getenv("DB_USER", "user")
    db_password = os.getenv("DB_PASSWORD", "password")
    
    print("Waiting for database...")

    while True:
        try:
            conn = psycopg2.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password
            )
            conn.close()
            print("Database is ready!")
            break
        except Exception:
            print("Database not ready, retrying...")
            time.sleep(2)



def init_db(conn):
    print("Creating table...")

    query = """
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        postId INTEGER,
        name TEXT,
        email TEXT,
        body TEXT
    );
    """

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

    print("Table ready.")


def insert_data(conn, comments):
    print("Inserting data...")

    cur = conn.cursor()

    for c in comments:
        cur.execute(
            """
            INSERT INTO comments (id, postId, name, email, body)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (c["id"], c["postId"], c["name"], c["email"], c["body"])
        )

    conn.commit()
    cur.close()

    print("Data inserted.")
