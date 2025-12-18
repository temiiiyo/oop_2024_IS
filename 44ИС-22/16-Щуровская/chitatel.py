class Chitatel:
    def __init__(self, id_chitatel, familia, name_chitatel, otchestvo, number_bulet):
        """Инициализация объекта Chitatel.
        """
        self._id_chitatel = id_chitatel
        self._familia = familia
        self._name_chitatel = name_chitatel
        self._otchestvo = otchestvo
        self._number_bulet = number_bulet

    @property
    def id_chitatel(self):
        """Получить идентификатор читателя."""
        return self._id_chitatel

    @property
    def familia(self):
        """Получить фамилию читателя."""
        return self._familia

    @familia.setter
    def familia(self, value):
        """Установить фамилию читателя."""
        self._familia = value

    @property
    def name_chitatel(self):
        """Получить имя читателя."""
        return self._name_chitatel

    @property
    def otchestvo(self):
        """Получить отчество читателя."""
        return self._otchestvo

    @property
    def number_bulet(self):
        """Получить номер билета читателя."""
        return self._number_bulet

    def __str__(self):
        return f"{self.id_chitatel} {self.familia} ({self.name_chitatel}, {self.otchestvo}, {self.number_bulet})"

    def __eq__(self, other):
        """Сравнивает два объекта  на равенство."""
        if isinstance(other, Chitatel):
            return self.id_chitatel == other.id_chitatel
        return False

    def __len__(self):
        """Возвращает длину, основанную на строках фамилии, имени и отчества."""
        return len(self.familia) + len(self.name_chitatel) + len(self.otchestvo)

    def __add__(self, other):
        """Складывает два объекта,  возвращая новый объект Chitatel."""
        if isinstance(other, Chitatel):
            combined_familia = self.familia + " & " + other.familia
            combined_name = self.name_chitatel + " & " + other.name_chitatel
            combined_otchestvo = self.otchestvo + " & " + other.otchestvo
            combined_id = str(self.id_chitatel) + " and " + str(other.id_chitatel)
            return Chitatel(combined_id, combined_familia, combined_name, combined_otchestvo, self.number_bulet)
        return NotImplemented
if __name__ == '__main__':
    pass