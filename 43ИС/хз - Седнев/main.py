import pandas as pd

class FurnitureType:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Furniture:
    def __init__(self, id, name, type_id, weight):
        self.id = id
        self.name = name
        self.type_id = type_id
        self.weight = weight

class Client:
    def __init__(self, id, name, phone, email, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Order:
    def __init__(self, id, client_id, furniture_list, delivery_address, status):
        self.id = id
        self.client_id = client_id
        self.furniture_list = furniture_list  # Список объектов Furniture
        self.delivery_address = delivery_address
        self.status = status

# Пример данных для типов мебели
types = [
    FurnitureType(1, "Стол", "Деревянный обеденный стол"),
    FurnitureType(2, "Стул", "Удобный стул для кухни"),
    FurnitureType(3, "Диван", "Большой кожаный диван")
]

# Пример данных для мебели
furniture = [
    Furniture(1, "Стол обеденный", 1, 25),
    Furniture(2, "Стул кухонный", 2, 7),
    Furniture(3, "Диван кожаный", 3, 50)
]

# Пример данных для клиентов
clients = [
    Client(1, "Иван Иванов", "123-456-789", "ivan@mail.com", "Москва, ул. Ленина, д. 1"),
    Client(2, "Мария Петрова", "987-654-321", "maria@mail.com", "Москва, ул. Тверская, д. 5")
]

# Пример данных для заказов
orders = [
    Order(1, 1, [furniture[0], furniture[1]], "Москва, ул. Ленина, д. 1", "Выполнен"),
    Order(2, 2, [furniture[1], furniture[2]], "Москва, ул. Тверская, д. 5", "Не выполнен"),
    Order(3, 1, [furniture[0], furniture[2]], "Москва, ул. Ленина, д. 1", "Не выполнен")
]

# Фильтрация невыполненных заказов
unfinished_orders = [order for order in orders if order.status != "Выполнен"]

# Создаем список для отчета
report_data = []

# Для каждого невыполненного заказа
for order in unfinished_orders:
    for furniture_item in order.furniture_list:
        # Находим тип мебели по ID
        furniture_type = next((type_ for type_ in types if type_.id == furniture_item.type_id), None)
        if furniture_type:
            report_data.append({
                "Заказ ID": order.id,
                "Клиент": next(client.name for client in clients if client.id == order.client_id),
                "Мебель": furniture_item.name,
                "Тип мебели": furniture_type.name,
                "Описание типа мебели": furniture_type.description,
                "Адрес доставки": order.delivery_address
            })

# Создаем DataFrame для отчета
df_report = pd.DataFrame(report_data)

# Сохраняем отчет в Excel
df_report.to_excel("unfinished_orders_report.xlsx", index=False)
print("Отчет сохранен!")

