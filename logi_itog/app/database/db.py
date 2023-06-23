import psycopg2
from config import host, user, password, db_name

connection = None  # Initialize connection variable

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name  # Correct parameter name to 'dbname'
    )

    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                ip_l varchar(50) not null,
                req_date date not null);"""
        )
        print("Table created")

except Exception as ex:
    print("Error:", ex)

finally:
    if connection:
        connection.close()
    print("Good")
