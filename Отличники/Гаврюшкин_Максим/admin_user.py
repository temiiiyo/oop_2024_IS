"""
Базовый Модуль для администратора библиотеки.
Выполнил: Гаврюшкин Максим 41ИС-21
"""
from user import User

class AdminUser(User):
    """Класс, представляющий административного пользователя библиотеки.

    Расширяет базовый класс User и добавляет методы для управления книгами и категориями.
    """

    def view_books(self):
        """Отображает все книги в библиотеке."""
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Available: {'Yes' if book[4] else 'No'}")

    def add_book(self, title, author, year):
        """Добавляет новую книгу в базу данных.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год публикации книги.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", (title, author, year, True))
            conn.commit()
            print(f"Книга '{title}' добавлена успешно.")

    def assign_category(self, book_id, category_id):
        """Назначает книгу определенной категории.

        Args:
            book_id (int): Идентификатор книги.
            category_id (int): Идентификатор категории.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO book_categories (book_id, category_id) VALUES (?, ?)", (book_id, category_id))
            conn.commit()
            print(f"Книга {book_id} добавлена к категории ID {category_id}.")
