class Book:
    book_count = 0  # Класс-атрибут для учета количества книг

    def __init__(self, id_book, name_book, name_author, genre, year):
        """Инициализирует экземпляр класса Book."""
        self.id_book = id_book
        self.name_book = name_book
        self.name_author = name_author
        self.genre = genre
        self.year = year
        Book.book_count += 1  # Увеличиваем счетчик при создании новой книги

    @property
    def id_book(self):
        """Возвращает идентификатор книги."""
        return self._id_book

    @property
    def name_book(self):
        """Возвращает название книги."""
        return self._name_book

    @property
    def name_author(self):
        """Возвращает имя автора книги."""
        return self._name_author

    @property
    def genre(self):
        """Возвращает жанр книги."""
        return self._genre

    @property
    def year(self):
        """Возвращает год публикации книги."""
        return self._year

    @id_book.setter
    def id_book(self, value):
        """Устанавливает идентификатор книги."""
        self._id_book = value

    @name_book.setter
    def name_book(self, value):
        """Устанавливает название книги."""
        self._name_book = value

    @name_author.setter
    def name_author(self, value):
        """Устанавливает имя автора книги."""
        self._name_author = value

    @genre.setter
    def genre(self, value):
        """Устанавливает жанр книги."""
        self._genre = value

    @year.setter
    def year(self, value):
        """Устанавливает год публикации книги."""
        self._year = value

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f"{self.id_book} {self.name_book} {self.name_author}, {self.genre}, {self.year}"

    def __eq__(self, other):
        """Проверяет равенство двух книг по их идентификаторам."""
        if isinstance(other, Book):
            return self.id_book == other.id_book
        return NotImplemented

    def __len__(self):
        """Возвращает длину названия книги."""
        return len(self.name_book)

    def __add__(self, other):
        """Объединяет две книги."""
        if isinstance(other, Book):
            new_id = max(self.id_book, other.id_book) + 1
            combined_name = f"{self.name_book} & {other.name_book}"
            combined_author = f"{self.name_author} and {other.name_author}"
            combined_genre = f"{self.genre}, {other.genre}"
            combined_year = (self.year, other.year)
            return Book(new_id, combined_name, combined_author, combined_genre, combined_year)
        return NotImplemented

    @classmethod
    def get_book_count(cls):
        """Возвращает количество книг."""
        return cls.book_count


if __name__ == '__main__':
    book1 = Book(1, "1984", "Джорд Оурел", "Фантастика", 1949)
    book2 = Book(2, "Мастер и Маргарита", "Михаил Булгаков", "роман", 1932)

    print("Количество книг:", Book.get_book_count())  # Вывод количества книг
