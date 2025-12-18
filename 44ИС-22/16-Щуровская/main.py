from datetime import datetime
from book import Book
from chitatel import Chitatel
from vidacha import Vidacha

def read_books_from_file(filename):
    """Читает данные о книгах из файла и возвращает список книг."""
    books = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) < 5:
                    print(f"Некорректная строка в файле {filename}: {line.strip()}")
                    continue
                id_book, name_book, name_author, genre, year_str = parts
                try:
                    year = int(year_str)
                    id_book_int = int(id_book)
                except ValueError:
                    print(f"Некорректное число в строке: {line.strip()}")
                    continue
                books.append(Book(id_book_int, name_book, name_author, genre, year))
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return books

def read_readers_from_file(filename):
    """Читает данные о читателях из файла и возвращает список читателей."""
    readers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) < 5:
                    print(f"Некорректная строка в файле {filename}: {line.strip()}")
                    continue
                id_chitatel_str, familia, name_chitatel, otchestvo, number_bulet = parts
                try:
                    id_chitatel = int(id_chitatel_str)
                except ValueError:
                    print(f"Некорректный номер читателя: {line.strip()}")
                    continue
                readers.append(Chitatel(id_chitatel, familia, name_chitatel, otchestvo, number_bulet))
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return readers

def read_issued_records_from_file(filename):
    """Читает записи о выдаче из файла и возвращает список записей."""
    issued_records = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) < 3:
                    print(f"Некорректная строка в файле {filename}: {line.strip()}")
                    continue
                id_chitatel_str, id_book_str, data_vidachi = parts
                try:
                    id_chitatel = int(id_chitatel_str)
                    id_book = int(id_book_str)
                except ValueError:
                    print(f"Некорректные номера в строке: {line.strip()}")
                    continue
                issued_records.append(Vidacha(id_chitatel, id_book, data_vidachi))
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return issued_records

def filter_issued_records(issued_records, start_date, end_date):
    """Фильтрует записи о выдаче по диапазону дат."""
    filtered_records = []
    for record in issued_records:
        try:
            date_of_issue = datetime.strptime(record.data_vidachi, '%Y-%m-%d')
        except ValueError:
            print(f"Некорректный формат даты: {record.data_vidachi}")
            continue
        if start_date <= date_of_issue <= end_date:
            filtered_records.append(record)
    return filtered_records

def write_filtered_records_to_file(filename, filtered_records, books, readers):
    """Записывает отфильтрованные записи с деталями в файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for record in filtered_records:
                book_info = next((book for book in books if book.id_book == record.id_book), None)
                reader_info = next((reader for reader in readers if reader.id_chitatel == record.id_chitatel), None)
                if book_info and reader_info:
                    file.write(f"{record.id_chitatel}; {reader_info.familia}; {reader_info.name_chitatel}; "
                               f"'{book_info.name_book}'; {record.data_vidachi}\n")
                else:
                    print(f"Не найдена книга или читатель для записи: {record}")
    except IOError as e:
        print(f"Ошибка при записи файла: {e}")

def main():
    # Задаем диапазон дат для фильтрации
    start_date_str = input("Введите начальную дату (ГГГГ-ММ-ДД): ").strip()
    end_date_str = input("Введите конечную дату (ГГГГ-ММ-ДД): ").strip()

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    except ValueError:
        print("Некорректный формат даты. Используйте ГГГГ-ММ-ДД.")
        return

    # Чтение данных
    books = read_books_from_file('books.txt')
    readers = read_readers_from_file('readers.txt')
    issued_records = read_issued_records_from_file('vidachaa.txt')

    if not books or not readers or not issued_records:
        print("Некоторые данные не были загружены. Проверьте файлы.")
        return

    # Фильтрация
    filtered_records = filter_issued_records(issued_records, start_date, end_date)

    # Запись результата
    write_filtered_records_to_file('out.txt', filtered_records, books, readers)
    print(f"Обработано {len(filtered_records)} записей. Результат сохранен в 'out.txt'.")

if __name__ == '__main__':
    main()