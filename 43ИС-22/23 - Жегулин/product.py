class Product:
    """
    Класс, представляющий продукт.

    Атрибуты:
        id (int): Идентификатор продукта.
        name (str): Название продукта.
        price (float): Цена продукта.
        warranty_period (int): Гарантийный срок продукта в месяцах.
    """

    def __init__(self, id, name, price, warranty_period):
        """
        Инициализация нового продукта.

        Аргументы:
            id (int): Идентификатор продукта.
            name (str): Название продукта.
            price (float): Цена продукта.
            warranty_period (int): Гарантийный срок продукта в месяцах.
        """
        self.id = id
        self.name = name
        self.price = price
        self.warranty_period = warranty_period

    def __str__(self):
        """
        Строковое представление продукта.

        Возвращает:
            str: Строка с информацией о продукте.
        """
        return f"Продукт(ID: {self.id}, Название: {self.name}, Цена: {self.price}, Гарантийный срок: {self.warranty_period} месяцев)"

    def update_price(self, new_price):
        """
        Обновить цену продукта.

        Аргументы:
            new_price (float): Новая цена продукта.
        """
        self.price = new_price
        print(f"Цена обновлена на: {self.price}")

    def is_under_warranty(self, current_date):
        """
        Проверить, находится ли продукт на гарантии.

        Аргументы:
            current_date (str): Текущая дата в формате "YYYY-MM-DD".

        Возвращает:
            bool: True, если продукт на гарантии, иначе False.
        """
        from datetime import datetime
        warranty_end_date = datetime.strptime(current_date, "%Y-%m-%d")
        warranty_start_date = warranty_end_date.replace(year=warranty_end_date.year - self.warranty_period)
        return datetime.now() <= warranty_end_date
