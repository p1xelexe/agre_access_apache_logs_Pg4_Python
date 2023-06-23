import json
import psycopg2
from database.config import host, user, password, db_name


# Чтение данных из файла JSON
with open('logs.json') as file:
    data = json.load(file)

# Установка соединения с базой данных
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    dbname=db_name
)
connection.autocommit = True

# Создание таблицы, если она не существует
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        ip_l VARCHAR(50) NOT NULL,
        req_date DATE NOT NULL
    );
"""
with connection.cursor() as cursor:
    cursor.execute(create_table_query)

# Вставка данных в таблицу
insert_query = """
    INSERT INTO users (ip_l, req_date)
    VALUES (%s, %s);
"""
with connection.cursor() as cursor:
    for ip, date in zip(data['IPs'], data['Dates']):
        cursor.execute(insert_query, (ip, date))

# Закрытие соединения с базой данных
connection.close()
