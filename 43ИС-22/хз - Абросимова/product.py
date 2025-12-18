class Product:
    """Класс для представления товара."""

    def __init__(self, product_id, name):
        """Инициализация товара с идентификатором и названием.

        Args:
            product_id (int): Идентификатор товара.
            name (str): Название товара.
        """
        self._product_id = product_id
        self._name = name

    @property
    def product_id(self):
        """Геттер для идентификатора товара."""
        return self._product_id

    @property
    def name(self):
        """Геттер для названия товара."""
        return self._name

    @name.setter
    def name(self, value):
        """Сеттер для названия товара."""
        self._name = value

    def display_info(self):
        """Возвращает строку с информацией о товаре.

        Returns:
            str: Информация о товаре.
        """
        return f"ID товара: {self.product_id}, Название: {self.name}"

