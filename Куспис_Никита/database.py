#Подключение БД
import mysql.connector

def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bus_station"
        )
        return connection
    except mysql.connector.Error as err:
        raise ConnectionError(f"Ошибка подключения к базе данных: {err}")
