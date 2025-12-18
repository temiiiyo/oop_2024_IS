import pandas as pd
from datetime import datetime
import os


# Класс для представления информации о книге
class Book:
    def __init__(self, book_id, title, author, genre, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __repr__(self):
        return f"{self.title} ({self.author}, {self.genre}, {self.publication_year})"


# Класс для представления информации о читателе
class Reader:
    def __init__(self, reader_id, last_name, first_name, patronymic, ticket_number):
        self.reader_id = reader_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.ticket_number = ticket_number

    def __repr__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} ({self.ticket_number})"


# Класс для представления информации о выдаче книги
class Issue:
    def __init__(self, reader, book, issue_date):
        self.reader = reader
        self.book = book
        self.issue_date = issue_date

    def __repr__(self):
        return f"{self.reader} - {self.book} (Выдано: {self.issue_date.strftime('%d-%m-%Y')})"


# библиотека, которая управляет книгами, читателями и выдачей книг
class Library:
    def __init__(self, books_data, readers_data, issues_data):
        self.books = [Book(*book) for book in books_data]
        self.readers = [Reader(*reader) for reader in readers_data]
        self.issues = []

        #выдачи
        for issue_data in issues_data:
            reader = next(r for r in self.readers if r.reader_id == issue_data[0])
            book = next(b for b in self.books if b.book_id == issue_data[1])
            issue_date = datetime.strptime(issue_data[2], "%Y-%m-%d")
            self.issues.append(Issue(reader, book, issue_date))

    def get_issue_report(self, start_date, end_date, year=None):
        report = []
        for issue in self.issues:
            if year is None:
                if start_date <= issue.issue_date <= end_date:
                    report.append({
                        "Фамилия": issue.reader.last_name,
                        "Имя": issue.reader.first_name,
                        "Книга": issue.book.title,
                        "Автор": issue.book.author,
                        "Дата выдачи": issue.issue_date.strftime('%d-%m-%Y')
                    })
            elif issue.issue_date.year == year:
                report.append({
                    "Фамилия": issue.reader.last_name,
                    "Имя": issue.reader.first_name,
                    "Книга": issue.book.title,
                    "Автор": issue.book.author,
                    "Дата выдачи": issue.issue_date.strftime('%d-%m-%Y')
                })
        return report

    # Метод для сохранения отчета в Excel
    def save_report_to_excel(self, report, file_name="issue_book/discharge.xlsx"):
        if report:
            df = pd.DataFrame(report)
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            df.to_excel(file_name, index=False)
            print("\nЖурнал выдачи книг сохранен в Excel!")
        else:
            print("Не найдено записей для данного года.")


#ЧТЕНИЕ ИНФОРМАЦИИ ИЗ ФАЙЛА

def read_data_from_txt(file_path):
    books = []
    readers = []
    issues = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()

        # Чтение книг
        books_section = data[data.index('books:') + 1:data.index('readers:')]
        for line in books_section:
            if line.strip():  # Проверка на пустую строку
                parts = line.split('|')
                if len(parts) == 5:  # Проверка на количество данных в строке
                    book_id, title, author, genre, year = parts
                    books.append((int(book_id), title, author, genre, int(year)))
                else:
                    print(f"Неверный формат строки в раздел books: {line}")

        # Чтение читателей
        readers_section = data[data.index('readers:') + 1:data.index('issues:')]
        for line in readers_section:
            if line.strip():  # Проверка на пустую строку
                parts = line.split('|')
                if len(parts) == 5:  # Проверка на количество данных в строке
                    reader_id, last_name, first_name, patronymic, ticket_number = parts
                    readers.append((int(reader_id), last_name, first_name, patronymic, ticket_number))
                else:
                    print(f"Неверный формат строки в раздел readers: {line}")

        # Чтение выдач
        issues_section = data[data.index('issues:') + 1:]
        for line in issues_section:
            if line.strip():  # Проверка на пустую строку
                parts = line.split('|')
                if len(parts) == 3:  # Проверка на количество данных в строке
                    reader_id, book_id, issue_date = parts
                    issues.append((int(reader_id), int(book_id), issue_date))
                else:
                    print(f"Неверный формат строки в раздел issues: {line}")

    return books, readers, issues


# Загрузка данных из текстового файла
books_data, readers_data, issues_data = read_data_from_txt("data.txt")

# Создаем библиотеку
library = Library(books_data, readers_data, issues_data)

# Ввод года пользователем
year_input = input("Введите год для фильтрации (или 'All' для всех записей): ")

# Обработка ввода
if year_input.lower() == "all":
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2024, 12, 31)
    report = library.get_issue_report(start_date, end_date)
else:
    try:
        year = int(year_input)
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        report = library.get_issue_report(start_date, end_date, year)
    except ValueError:
        print("Неверный формат ввода года!")
        report = []

# Вывод в консоль
print(f"\nЖурнал выдачи книг за {year_input} год:")
for entry in report:
    print(
        f"{entry['Фамилия']} {entry['Имя']} - {entry['Книга']} ({entry['Автор']}) - Дата выдачи: {entry['Дата выдачи']}")

# Сохранение в Excel через метод класса Library
library.save_report_to_excel(report)
