import psycopg2

try:
    # Connect to an existing database
    conn_db = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port="5432", database="suppliers")
    
    # Create a cursor to perform database operations
    cur = conn_db.cursor()
    # print PostgreSQL details
    print("PostgreSQL server inforamtion")
    print(conn_db.get_dsn_parameters(), "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (conn_db):
        cur.close()
        conn_db.close()
        print("PostgeSQL connection closed")