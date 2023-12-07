import psycopg2

try:
    conn_db = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port="5432", database="suppliers")
    cur = conn_db.cursor()
    
    insert_query = """INSERT INTO mobile (ID, MODEL, PRICE) VALUES
        (1, 'iPhone12', 1100);
    """
    cur.execute(insert_query)
    conn_db.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cur.execute("SELECT * FROM mobile;")
    record = cur.fetchall()
    print("Result:", record)
    
    
    # Executing a SQL query to update table
    update_query = """Update mobile set price = 1500 where id = 1"""
    cur.execute(update_query)
    conn_db.commit()
    count = cur.rowcount
    print(count, "Record updated successfully ")
    # Fetch result
    cur.execute("SELECT * from mobile")
    print("Result ", cur.fetchall())

    # Executing a SQL query to delete table
    delete_query = """Delete from mobile where id = 1"""
    cur.execute(delete_query)
    conn_db.commit()
    count = cur.rowcount
    print(count, "Record deleted successfully ")
    # Fetch result
    cur.execute("SELECT * from mobile")
    print("Result ", cur.fetchall())
    
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    conn_db.rollback()
finally:
    if conn_db:
        cur.close()
        conn_db.close()
        print("PostgreSQL connection is closed")