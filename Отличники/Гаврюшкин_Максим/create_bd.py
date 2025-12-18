"""
Создание структуры базы данных.
Выполнил: Гаврюшкин Максим 41ИС-21
"""
import sqlite3

def create_database():
    # Подключение к базе данных (если файла базы данных нет, он будет создан)
    conn = sqlite3.connect('complex_library.db')
    cursor = conn.cursor()

    # Создание таблицы ролей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            role_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT UNIQUE NOT NULL
        )
    ''')

    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role_id INTEGER,
            FOREIGN KEY (role_id) REFERENCES roles(role_id)
        )
    ''')

    # Создание таблицы книг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            available BOOLEAN DEFAULT 1
        )
    ''')

    # Создание таблицы категорий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL
        )
    ''')

    # Создание таблицы для связи книг и категорий (многие ко многим)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_categories (
            book_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (book_id, category_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id),
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')

    # Создание таблицы транзакций (аренда книг)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            date_issued DATE NOT NULL,
            date_due DATE,
            date_returned DATE,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')

    # Заполнение таблицы ролей начальными данными
    cursor.execute("INSERT OR IGNORE INTO roles (role_name) VALUES ('admin'), ('librarian'), ('reader')")

    # Завершение и сохранение изменений
    conn.commit()
    conn.close()
    print("Создание или измение структуры завершено!")

# Запуск функции для создания базы данных
if __name__ == "__main__":
    create_database()
