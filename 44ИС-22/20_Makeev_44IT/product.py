# product.py
"""Модуль с классом Product, представляющим товар."""


class Product:
    """
    Представляет товар в магазине.

    Атрибуты:
        _id (int): Уникальный идентификатор товара.
        _name (str): Название товара.
        _price (float): Цена товара.
        _quantity (int): Количество товара на складе.
    """

    def __init__(self, id: int, name: str, price: float, quantity: int):
        """
        Инициализирует объект Product.

        Args:
            id (int): Уникальный идентификатор товара.
            name (str): Название товара.
            price (float): Цена товара.
            quantity (int): Количество товара на складе.
        """
        self._id = id
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_id(self) -> int:
        """Возвращает идентификатор товара."""
        return self._id

    def get_name(self) -> str:
        """Возвращает название товара."""
        return self._name

    def get_price(self) -> float:
        """Возвращает цену товара."""
        return self._price

    def get_quantity(self) -> int:
        """Возвращает количество товара на складе."""
        return self._quantity

    def set_quantity(self, quantity: int):
        """Устанавливает новое количество товара на складе.

        Args:
            quantity (int): Новое количество товара.
        """
        self._quantity = quantity

    def __eq__(self, other: object) -> bool:
        """Сравнивает два объекта Product по их id.

        Args:
            other (object): Объект для сравнения.

        Returns:
             bool: True, если id совпадают, False в противном случае.
        """
        if not isinstance(other, Product):
            return False
        return self._id == other._id

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Product."""
        return f"ID: {self._id}, Название: {self._name}, Цена: {self._price}, Количество: {self._quantity}"

    @classmethod
    def create_from_list(cls, data: list) -> 'Product':
        """Создает объект Product из списка.

         Args:
             data (list): Список данных [id, name, price, quantity]
        Returns:
             Product: Созданный продукт.
        """
        if len(data) != 4:
            raise ValueError("Invalid list length for Product creation")
        return cls(id=data[0], name=data[1], price=data[2], quantity=data[3])


def load_products_from_file(filename):
    """Загружает продукты из файла."""
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, quantity = line.strip().split(',')
                products.append(Product(int(id), name, float(price), int(quantity)))
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return products


if __name__ == "__main__":
    products = load_products_from_file('products.txt')