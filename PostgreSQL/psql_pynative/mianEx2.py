import datetime

import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port="5432", database="suppliers")

    cursor = connection.cursor()
    # Executing a SQL query to insert datetime into table
    insert_query = """ INSERT INTO item (item_Id, item_name, purchase_time, price) VALUES (%s, %s, %s, %s)"""
    item_purchase_time = datetime.datetime.now()
    item_tuple = (13, "Keyboard", item_purchase_time, 150)
    cursor.execute(insert_query, item_tuple)
    connection.commit()
    print("1 item inserted successfully")

    # Read PostgreSQL purchase timestamp value into Python datetime
    cursor.execute("SELECT purchase_time from item where item_id = 12")
    purchase_datetime = cursor.fetchone()
    print("Item Purchase date is  ", purchase_datetime[0])
    print("Item Purchase time is  ", purchase_datetime[0].date())

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")