"""
Базовый Модуль для посетителя библиотеки.
Выполнил: Гаврюшкин Максим 41ИС-21
"""
from datetime import datetime, timedelta
from user import User

class RegularUser(User):
    """Класс, представляющий обычного пользователя библиотеки.

    Расширяет базовый класс User и добавляет методы для просмотра и заимствования книг.
    """

    def view_books(self):
        """Отображает доступные для заимствования книги."""
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE available = 1")
            books = cursor.fetchall()
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Наличие: {'Да' if book[4] else 'Нет'}")

    def borrow_book(self, book_id):
        """Позволяет пользователю взять книгу в аренду.

        Args:
            book_id (int): Идентификатор книги для заимствования.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT available FROM books WHERE book_id = ?", (book_id,))
            book = cursor.fetchone()
            if book and book[0]:
                date_issued = datetime.now().date()
                date_due = date_issued + timedelta(days=14)
                cursor.execute("INSERT INTO transactions (user_id, book_id, date_issued, date_due) VALUES (?, ?, ?, ?)",
                               (self.get_user_id(), book_id, date_issued, date_due))
                cursor.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
                conn.commit()
                print(f"Идентификатор книги {book_id} был успешно заимствован.")
            else:
                print("Книга недоступна.")

    def get_user_id(self):
        """Возвращает идентификатор текущего пользователя.

        Returns:
            int: Идентификатор пользователя или None, если пользователь не найден.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (self._username,))
            user = cursor.fetchone()
            return user[0] if user else None
