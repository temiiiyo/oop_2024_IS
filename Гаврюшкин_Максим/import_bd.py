"""
Добавление данных в Базу Данных.
Выполнил: Гаврюшкин Максим 41ИС-21
"""
import sqlite3
from datetime import datetime, timedelta

def populate_test_data():
    # Подключение к базе данных
    conn = sqlite3.connect('complex_library.db')
    cursor = conn.cursor()

    # Добавление тестовых пользователей
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role_id) VALUES ('admin_user', 'admin_pass', 1)")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role_id) VALUES ('librarian_user', 'librarian_pass', 2)")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role_id) VALUES ('reader_user', 'reader_pass', 3)")

    # Добавление тестовых книг
    cursor.execute("INSERT OR IGNORE INTO books (title, author, year, available) VALUES ('1984', 'George Orwell', 1949, 1)")
    cursor.execute("INSERT OR IGNORE INTO books (title, author, year, available) VALUES ('Brave New World', 'Aldous Huxley', 1932, 1)")
    cursor.execute("INSERT OR IGNORE INTO books (title, author, year, available) VALUES ('Fahrenheit 451', 'Ray Bradbury', 1953, 1)")

    # Добавление тестовых категорий
    cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES ('Dystopian')")
    cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES ('Science Fiction')")
    cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES ('Classic')")

    # Добавление связей между книгами и категориями (многие ко многим)
    cursor.execute("INSERT OR IGNORE INTO book_categories (book_id, category_id) VALUES (1, 1)")
    cursor.execute("INSERT OR IGNORE INTO book_categories (book_id, category_id) VALUES (2, 2)")
    cursor.execute("INSERT OR IGNORE INTO book_categories (book_id, category_id) VALUES (3, 3)")

    # Добавление тестовых транзакций
    date_issued = datetime.now().date()
    date_due = date_issued + timedelta(days=14)
    cursor.execute("INSERT OR IGNORE INTO transactions (user_id, book_id, date_issued, date_due) VALUES (3, 1, ?, ?)", (date_issued, date_due))

    # Завершение и сохранение изменений
    conn.commit()
    conn.close()
    print("Test data added successfully!")

# Запуск функции для заполнения таблиц тестовыми данными
if __name__ == "__main__":
    populate_test_data()
