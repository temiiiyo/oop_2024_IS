import sqlite3
import os

DB_NAME = 'telephone_station.db'

def connect_db():
    """Создание подключения к базе данных SQLite"""
    try:
        conn = sqlite3.connect(DB_NAME)
        # Включаем поддержку внешних ключей
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def execute_query(query, params=None):
    """Выполнение SQL-запроса без возврата данных (INSERT, UPDATE, DELETE)"""
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return True
        except Exception as e:
            print(f"Ошибка выполнения SQL-запроса: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

def fetch_data(query, params=None):
    """Выполнение SQL-запроса с возвратом данных (SELECT)"""
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Ошибка выполнения SQL-запроса: {e}")
            return []
        finally:
            cursor.close()
            connection.close()