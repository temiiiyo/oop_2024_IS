"""
Базовый Модуль для всех пользователей библиотеки.
Выполнил: Гаврюшкин Максим 41ИС-21
"""
import sqlite3
from abc import ABC, abstractmethod

class User(ABC):
    """Базовый класс для пользователей библиотеки.

    Содержит базовые атрибуты и методы для работы с системой.
    """

    def __init__(self, username, password):
        """Инициализирует пользователя с именем и паролем.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.
        """
        self._username = username
        self._password = password

    def connect_db(self):
        """Создает и возвращает соединение с базой данных.

        Returns:
            sqlite3.Connection: Объект соединения с базой данных.
        """
        return sqlite3.connect('complex_library.db')

    @abstractmethod
    def view_books(self):
        """Абстрактный метод для просмотра книг."""
        pass
