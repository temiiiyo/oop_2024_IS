class Vidacha:
    """Класс для представления информации о выдаче книги читателю."""

    def __init__(self, id_chitatel, id_book, data_vidachi):
        """Инициализирует экземпляр класса Vidacha.
        """
        self._id_chitatel = id_chitatel
        self._id_book = id_book
        self._data_vidachi = data_vidachi

    @property
    def id_chitatel(self):
        """Возвращает идентификатор читателя."""
        return self._id_chitatel

    @property
    def id_book(self):
        """Возвращает идентификатор книги."""
        return self._id_book

    @property
    def data_vidachi(self):
        """Возвращает дату выдачи книги."""
        return self._data_vidachi

    # Сеттеры
    @id_chitatel.setter
    def id_chitatel(self, value):
        """Устанавливает идентификатор читателя.
        """
        self._id_chitatel = value

    @id_book.setter
    def id_book(self, value):
        """Устанавливает идентификатор книги.
        """
        self._id_book = value

    @data_vidachi.setter
    def data_vidachi(self, value):
        """Устанавливает дату выдачи книги.
        """
        self._data_vidachi = value

    def __str__(self):
        """Возвращает строковое представление экземпляра Vidacha."""
        return f"{self.id_chitatel} {self.id_book} ({self.data_vidachi})"

    def __eq__(self, other):
        """Сравнивает два экземпляра Vidacha на равенство.
        """
        if not isinstance(other, Vidacha):
            return NotImplemented
        return (self.id_chitatel == other.id_chitatel and
                self.id_book == other.id_book and
                self.data_vidachi == other.data_vidachi)

    def __len__(self):
        """Возвращает длину строки data_vidachi.
        """
        return len(self.data_vidachi)

    def __add__(self, other):
        """Создает новый экземпляр Vidacha, объединяя данные двух экземпляров.
        """
        if not isinstance(other, Vidacha):
            return NotImplemented
        # Например, создаем новую Vidacha с атрибутами
        return Vidacha(self.id_chitatel, self.id_book,
                       f"{self.data_vidachi} + {other.data_vidachi}")

if __name__ == '__main__':
    pass