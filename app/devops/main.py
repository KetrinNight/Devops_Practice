import os
import time
import psycopg2

def create_connection():
    """Создает и возвращает соединение с базой данных."""
    return psycopg2.connect(
        database=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOSTNAME"),
        port=int(os.getenv("POSTGRES_PORT", default="5432"))
    )

def create_table(cursor):
    """Создает таблицу в базе данных."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id serial PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            hashed_password VARCHAR(128) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_admin BOOLEAN DEFAULT FALSE
        );
    """)

def insert_data(cursor, username, hashed_password):
    """Вставляет данные в таблицу."""
    cursor.execute("""
        INSERT INTO users (username, hashed_password) 
        VALUES (%s, %s)
    """, (username, hashed_password))

def fetch_data(cursor):
    """Извлекает данные из таблицы."""
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def main():
    connection = create_connection()
    cursor = connection.cursor()

    create_table(cursor)
    insert_data(cursor, 'example_user', '5f4dcc3b5aa765d61d8327deb882cf99')
    records = fetch_data(cursor)

    print("Data: ", records)

    connection.commit()
    cursor.close()
    connection.close()

