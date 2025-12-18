from product import Product


class ProductManager:
    """Класс для управления товарами."""

    def __init__(self):
        """Инициализация менеджера товаров."""
        self.products = {}

    def load_p_file(self, filename):
        """Загружает товары из файла.

        Args:
            filename (str): Имя файла для загрузки товаров.
        """
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                product_id, name = line.strip().split(',')
                self.products[int(product_id)] = Product(int(product_id), name)

    def get_product(self, product_id):
        """Возвращает товар по его идентификатору.

        Args:
            product_id (int): Идентификатор товара.

        Returns:
            Product: Объект товара или None, если товар не найден.
        """
        return self.products.get(product_id)

