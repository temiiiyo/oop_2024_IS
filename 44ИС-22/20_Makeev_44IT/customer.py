# online_store/customer.py
"""Модуль с классом Customer, представляющим клиента."""


class Customer:
    """
    Представляет клиента.

    Атрибуты:
        _id (int): Уникальный идентификатор клиента.
        _name (str): Имя клиента.
        _address (str): Адрес клиента.
    """

    def __init__(self, id: int, name: str, address: str):
        """
        Инициализирует объект Customer.

        Args:
            id (int): Уникальный идентификатор клиента.
            name (str): Имя клиента.
            address (str): Адрес клиента.
        """
        self._id = id
        self._name = name
        self._address = address

    def get_id(self) -> int:
        """Возвращает идентификатор клиента."""
        return self._id

    def get_name(self) -> str:
        """Возвращает имя клиента."""
        return self._name

    def set_name(self, name: str):
        """Устанавливает имя клиента."""
        self._name = name

    def get_address(self) -> str:
        """Возвращает адрес клиента."""
        return self._address

    def set_address(self, address: str):
        """Устанавливает адрес клиента."""
        self._address = address

    def __eq__(self, other: object) -> bool:
        """Сравнивает два объекта Customer по их id.

        Args:
            other (object): Объект для сравнения.

        Returns:
            bool: True, если id совпадают, False в противном случае.
        """
        if not isinstance(other, Customer):
            return False
        return self._id == other._id

    def __str__(self) -> str:
        """Возвращает строковое представление клиента."""
        return f"ID: {self._id}, Name: {self._name}, Address: {self._address}"

    @classmethod
    def create_from_tuple(cls, data: tuple) -> 'Customer':
        """Создает объект Customer из кортежа.

        Args:
           data (tuple): Кортеж с данными (id, name, address)
        Returns:
            Customer: Созданный клиент.
        """
        if len(data) != 3:
            raise ValueError("Invalid tuple length for Customer creation")
        return cls(id=data[0], name=data[1], address=data[2])


if __name__ == "__main__":
    customer1 = Customer(1, "Test Customer 1", "Test Address 1")
    print(customer1)
    customer2 = Customer(2, "Test Customer 2", "Test Address 2")
    print(f"customer1 == customer2: {customer1 == customer2}")
    customer3 = Customer(1, "Test Customer 1", "Test Address 1")
    print(f"customer1 == customer3: {customer1 == customer3}")
    customer1.set_address("New test Address")
    print(f"customer1 after set_address: {customer1}")
    customer1.set_name("New Name")
    print(f"customer1 after set_name: {customer1}")

    customer4 = Customer.create_from_tuple((3, "Test Customer 3", "Test Address 3"))
    print(f"customer4 from class method: {customer4}")