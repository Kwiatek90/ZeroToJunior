import psycopg2
from configparser import ConfigParser

path = "D:\Programowanie\ZeroToJunior\PostgreSQL\psql_tutorial\database.ini"
def config(filename=path, section="postgresql"):
    # create a parser
    parser = ConfigParser()
    parser.read(filename)
    
    # get section, default postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

def connect():
    """Connect to the PostgreSQL database server"""
    conn_db = None
    try:
        #read connection parameters
        params = config()
        conn_db = psycopg2.connect(**params)
        
        #create cursor
        cur = conn_db.cursor()
        cur.execute("SELECT version()")
        
        #recv the data from db
        data =  cur.fetchone()
        print(data)
        
        #close conn wit postgre
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn_db is not None:
            conn_db.close()
            print('Database connection closed.')
#conn_db =  psycopg2.connect(host="127.0.0.1", database="suppliers", user="postgres", password="admin")

if __name__ == '__main__':
    connect()
