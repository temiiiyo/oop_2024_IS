class WarrantyReceptionist:
    def __init__(self, name):
        self.name = name

    def accept_product(self, product, client):
        if not product.is_under_warranty():
            return f"Продукт {product.name} клиента {client.name} не подлежит гарантии."
        return f"Продукт {product.name} принят у клиента {client.name} для анализа."