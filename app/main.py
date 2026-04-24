import psycopg2

from dbutils import *
from datautils import *


def main():

    wait_for_db()

    comments = fetch_comments()

    conn = get_conn()

    init_db(conn)

    insert_data(conn, comments)

    result = group_by_post_id(comments)

    save_results(result)

    conn.close()



#    conn = psycopg2.connect(
#        host=DB_HOST,
#        database=DB_NAME,
#        user=DB_USER,
#        password=DB_PASSWORD
#    )

#    comments = fetch_comments()

#    init_db(conn)
#    insert_data(conn, comments)

#    grouped = group_by_post_id(comments)
#    save_results(grouped)

#    conn.close()

    print("Done.")


if __name__ == "__main__":
    main() 
