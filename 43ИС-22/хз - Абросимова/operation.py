class Operation:
    """Класс для представления операции."""

    def __init__(self, o_type):
        """Инициализация операции с типом.

        Args:
            o_type (str): Тип операции.
        """
        self._o_type = o_type

    @property
    def o_type(self):
        """Геттер для типа операции."""
        return self._o_type

    @o_type.setter
    def o_type(self, value):
        """Сеттер для типа операции."""
        self._o_type = value

    def d_info(self):
        """Возвращает строку с информацией об операции.

        Returns:
            str: Информация об операции.
        """
        return f"Тип операции: {self.o_type}"
