"""
Задача - "LibrarySystem"
Описание задачи:
Разработать систему управления библиотекой на Python, которая:
1. Позволяет пользователям добавлять, обновлять и просматривать книги.
2. Разделяет роли пользователей: администратор имеет доступ к управлению книгами, а обычные пользователи могут только просматривать информацию и брать книгу.
3. Включает механизм наследования классов для реализации пользователей и администраторов.
4. Демонстрирует использование наследственности, инкапсуляции и полиморфизма.

Структура базы данных:
Предлагаемая база данных должна содержать следующие таблицы:

users – пользователи.
roles – роли пользователей.
books – книги.
categories – категории книг.
book_categories – связь книг и категорий.
transactions – информация об аренде книг.

Примечание1: Создание базы данных происходит в любом формате и любой среде, также код должен быть разделён по модулям.
Примечание2: Уровни оценок:
 5 баллов, если программа работает и выполнены все условия.
 4 балла, если программа работает и условия выполненны частично.
 3 балла, если программа работает, но максимально упрощена в написании кода и условия не выполнены.
 2 балла, если программа не работает.
 Выполнил: Гаврюшкин Максим 41ИС-21
"""

import sqlite3
from admin_user import AdminUser
from regular_user import RegularUser

def main():
    """Основная функция для взаимодействия с пользователем.

    Запрашивает ввод пользователя, проверяет роль и предоставляет соответствующий интерфейс.
    """
    print("Приветствуем в Advanced Library System")
    username = input("Введите имя пользователя: ")
    password = input("Введите пороль: ")

    with sqlite3.connect('complex_library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role_id FROM users WHERE username = ? AND password = ?", (username, password))
        user_data = cursor.fetchone()

    if user_data:
        role_id = user_data[0]
        if role_id == 1:  # Администратор
            user = AdminUser(username, password)
            while True:
                print("\n1. Просмотреть список книг\n2.Добавить книгу\n3. Присвоить категорию книги\n4. Выход")
                choice = input("Выберите выберите необходимое действие: ")
                if choice == '1':
                    user.view_books()
                elif choice == '2':
                    title = input("Введите название книги: ")
                    author = input("Введите имя автора: ")
                    year = int(input("Введите год выпуска: "))
                    user.add_book(title, author, year)
                elif choice == '3':
                    book_id = int(input("Введите ID книги: "))
                    category_id = int(input("Введите ID категории: "))
                    user.assign_category(book_id, category_id)
                elif choice == '4':
                    break
                else:
                    print("Неверный ввод. Пожалуйста, попробуйте снова.")
        elif role_id == 2:  # Обычный пользователь
            user = RegularUser(username, password)
            while True:
                print("\n1. Просмотр доступных книг\n2. Взять книгу\n3. Выход")
                choice = input("Выберите действие: ")
                if choice == '1':
                    user.view_books()
                elif choice == '2':
                    book_id = int(input("Введите ID выбираемой книги: "))
                    user.borrow_book(book_id)
                elif choice == '3':
                    break
                else:
                    print("Неверный ввод. Пожалуйста, попробуйте снова.")
    else:
        print("Неверное имя пользователя или пароль.")

if __name__ == "__main__":
    main()
