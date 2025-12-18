import json
from worker import Turner, Locksmith, Miller
from shop_chief import ShopChief
from shop import Shop
from factory import Factory


def create_worker(worker_data):
    """Создание работника на основе данных."""
    worker_type = worker_data["type"]
    name = worker_data["name"]
    age = worker_data["age"]

    if worker_type == "Turner":
        return Turner(name, age)
    elif worker_type == "Locksmith":
        return Locksmith(name, age)
    elif worker_type == "Miller":
        return Miller(name, age)
    else:
        raise ValueError(f"Неизвестный тип работника: {worker_type}")


def load_factory_from_file(file_path):
    """Загрузка данных завода из файла."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    factory_data = data["factory"]
    factory = Factory(factory_data["name"])

    for shop_data in factory_data["shops"]:
        chief_data = shop_data["chief"]
        chief = ShopChief(chief_data["name"], chief_data["age"], shop_data["name"])

        shop = Shop(shop_data["name"], chief)

        for worker_data in shop_data["workers"]:
            worker = create_worker(worker_data)
            shop.add_worker(worker)

        factory.add_shop(shop)

    return factory


if __name__ == "__main__":
    factory = load_factory_from_file("data.json")

    print(factory)
    for shop in factory.shops:
        print(shop)
        for worker in shop.workers:
            print(worker)
            print(worker.work())
        print(shop.chief.manage())