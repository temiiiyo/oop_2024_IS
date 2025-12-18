import sqlite3
from datetime import datetime


def create_database():
    """Создание базы данных и всех таблиц"""
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Создание таблицы ролей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roles (
        role_id INTEGER PRIMARY KEY AUTOINCREMENT,
        role_name VARCHAR(50) NOT NULL
    )
    ''')

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        password_hash VARCHAR(100) NOT NULL,
        role_id INTEGER,
        FOREIGN KEY (role_id) REFERENCES Roles(role_id)
    )
    ''')

    # Создание таблицы клиентов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(100) NOT NULL,
        passport_number VARCHAR(20),
        phone_number VARCHAR(20)
    )
    ''')

    # Создание таблицы валют
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Currency (
        currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(10) NOT NULL UNIQUE,
        sale_rate DECIMAL(10, 4) NOT NULL,
        buy_rate DECIMAL(10, 4) NOT NULL
    )
    ''')

    # Создание таблицы транзакций
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        currency_id INTEGER NOT NULL,
        amount DECIMAL(15, 2) NOT NULL,
        transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES Clients(client_id),
        FOREIGN KEY (currency_id) REFERENCES Currency(currency_id)
    )
    ''')

    # Создание представления CurrencyShare (доля каждой валюты)
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS CurrencyShare AS
    SELECT 
        c.name AS currency_name,
        SUM(t.amount * c.sale_rate) AS total_volume_rub,
        ROUND(SUM(t.amount * c.sale_rate) * 1.0 / (
            SELECT SUM(t2.amount * c2.sale_rate) 
            FROM Transactions t2 
            JOIN Currency c2 ON t2.currency_id = c2.currency_id
        ), 4) AS share
    FROM Transactions t
    JOIN Currency c ON t.currency_id = c.currency_id
    GROUP BY c.currency_id, c.name
    ''')

    # Создание представления MaxTransaction (максимальная сделка)
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS MaxTransaction AS
    SELECT 
        t.transaction_id,
        cl.full_name AS client_name,
        c.name AS currency_name,
        (t.amount * c.sale_rate) AS total_rub
    FROM Transactions t
    JOIN Clients cl ON t.client_id = cl.client_id
    JOIN Currency c ON t.currency_id = c.currency_id
    WHERE (t.amount * c.sale_rate) = (
        SELECT MAX(t2.amount * c2.sale_rate)
        FROM Transactions t2
        JOIN Currency c2 ON t2.currency_id = c2.currency_id
    )
    LIMIT 1
    ''')

    # Добавление тестовых данных
    add_test_data(cursor, conn)

    conn.commit()
    conn.close()
    print("База данных успешно создана!")


def add_test_data(cursor, conn):
    """Добавление тестовых данных в базу"""

    # Добавляем роли
    cursor.execute("SELECT COUNT(*) FROM Roles")
    if cursor.fetchone()[0] == 0:
        roles = [('Оператор',), ('Пользователь',)]
        cursor.executemany("INSERT INTO Roles (role_name) VALUES (?)", roles)

    # Добавляем пользователей
    cursor.execute("SELECT COUNT(*) FROM Users")
    if cursor.fetchone()[0] == 0:
        users = [
            ('admin', 'admin123', 1),  # Оператор
            ('user1', 'user123', 2),  # Пользователь
            ('user2', 'user456', 2)  # Пользователь
        ]
        cursor.executemany("INSERT INTO Users (username, password_hash, role_id) VALUES (?, ?, ?)", users)

    # Добавляем клиентов
    cursor.execute("SELECT COUNT(*) FROM Clients")
    if cursor.fetchone()[0] == 0:
        clients = [
            ('Иванов Иван Иванович', '4501 123456', '+7 (999) 123-45-67'),
            ('Петров Петр Петрович', '4502 234567', '+7 (999) 234-56-78'),
            ('Сидорова Анна Сергеевна', '4503 345678', '+7 (999) 345-67-89'),
            ('Козлов Алексей Викторович', '4504 456789', '+7 (999) 456-78-90')
        ]
        cursor.executemany("INSERT INTO Clients (full_name, passport_number, phone_number) VALUES (?, ?, ?)", clients)

    # Добавляем валюты
    cursor.execute("SELECT COUNT(*) FROM Currency")
    if cursor.fetchone()[0] == 0:
        currencies = [
            ('USD', 91.50, 90.00),  # Доллар США
            ('EUR', 99.80, 98.50),  # Евро
            ('CNY', 12.80, 12.50),  # Китайский юань
            ('GBP', 115.20, 114.00)  # Фунт стерлингов
        ]
        cursor.executemany("INSERT INTO Currency (name, sale_rate, buy_rate) VALUES (?, ?, ?)", currencies)

    # Добавляем транзакции
    cursor.execute("SELECT COUNT(*) FROM Transactions")
    if cursor.fetchone()[0] == 0:
        transactions = [
            (1, 1, 1000.00),  # Клиент 1, USD, 1000 долларов
            (2, 2, 500.00),  # Клиент 2, EUR, 500 евро
            (3, 1, 2500.00),  # Клиент 3, USD, 2500 долларов
            (4, 3, 10000.00),  # Клиент 4, CNY, 10000 юаней
            (1, 4, 800.00),  # Клиент 1, GBP, 800 фунтов
            (2, 1, 1500.00),  # Клиент 2, USD, 1500 долларов
            (3, 2, 750.00),  # Клиент 3, EUR, 750 евро
            (4, 3, 5000.00)  # Клиент 4, CNY, 5000 юаней
        ]
        cursor.executemany("INSERT INTO Transactions (client_id, currency_id, amount) VALUES (?, ?, ?)", transactions)

    conn.commit()


if __name__ == "__main__":
    create_database()