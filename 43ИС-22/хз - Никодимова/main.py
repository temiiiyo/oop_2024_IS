import json


class Shop:
    def __init__(self, name: str):
        self._name = name
        self.workers = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.remove(worker)

    def count_workers(self):
        return len(self.workers)


class Factory:
    def __init__(self, name: str):
        self._name = name
        self.shops = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_shop(self, shop):
        self.shops.append(shop)

    def remove_shop(self, shop):
        self.shops.remove(shop)

    def count_workers(self):
        return sum(shop.count_workers() for shop in self.shops)


class Worker:
    def __init__(self, name: str, age: int = 0, experience: int = 0):
        self._name = name
        self._age = age
        self._experience = experience

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("Стаж не может быть отрицательным")
        self._experience = value


class WorkerType(Worker): # Рабочий
    pass


class Foreman(Worker): # Начальник
    pass


class LatheOperator(WorkerType): # Токарь
    pass


class Fitter(WorkerType): # Слесарь
    pass


class Miller(WorkerType): # Фрезеровщик
    pass


def save_to_json(factory, filename):
    data = {
        'name': factory.name,
        'shops': []
    }

    for shop in factory.shops:
        shop_data = {
            'name': shop.name,
            'workers': [worker.name for worker in shop.workers]
        }
        data['shops'].append(shop_data)

    with open(filename, 'w') as f:
        json.dump(data, f)


def load_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    factory = Factory(data['name'])

    for shop_data in data['shops']:
        shop = Shop(shop_data['name'])
        for worker_name in shop_data['workers']:
            worker = Worker(worker_name)
            shop.add_worker(worker)
        factory.add_shop(shop)

    return factory


def menu():
    factory = None

    while True:
        print("\n1. Создать завод")
        print("2. Добавить цех")
        print("3. Добавить работника")
        print("4. Сохранить в JSON")
        print("5. Загрузить из JSON")
        print("6. Показать информацию о заводе")
        print("7. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            name = input("Введите название завода: ")
            factory = Factory(name)
            print(f"Завод '{factory.name}' создан.")

        elif choice == '2' and factory:
            name = input("Введите название цеха: ")
            shop = Shop(name)
            factory.add_shop(shop)
            print(f"Цех '{shop.name}' добавлен.")

        elif choice == '3' and factory:
            shop_name = input("Введите название цеха для добавления работника: ")
            shop = next((s for s in factory.shops if s.name == shop_name), None)
            if shop:
                worker_name = input("Введите имя работника: ")
                worker_type = input("Введите тип работника (Токарь/Слесарь/Фрезеровщик/Начальник цеха): ")
                Worker_age = int(input("Введите возраст сотрудника: "))
                Worker_experience = int(input("Введите опыт сотрудника: "))

                if worker_type.lower() == "токарь":
                    worker = LatheOperator(worker_name, Worker_age, Worker_experience)
                elif worker_type.lower() == "слесарь":
                    worker = Fitter(worker_name, Worker_age, Worker_experience)
                elif worker_type.lower() == "фрезеровщик":
                    worker = Miller(worker_name, Worker_age, Worker_experience)

                elif worker_type.lower() == "начальник цеха":
                    worker = Foreman(worker_name, Worker_age, Worker_experience)
                else:
                    print("Некорректный тип работника.")
                    continue

                shop.add_worker(worker)
                print(f"Работник '{worker.name}' добавлен в цех '{shop.name}'.")
            else:
                print("Цех не найден.")

        elif choice == '4' and factory:
            filename = input("Введите имя файла для сохранения: ")
            save_to_json(factory, filename)
            print(f"Данные сохранены в '{filename}'.")

        elif choice == '5':
            filename = input("Введите имя файла для загрузки: ")
            factory = load_from_json(filename)
            print(f"Данные загружены из '{filename}'.")

        elif choice == '6' and factory:
            print(f"Завод: {factory.name}")
            for shop in factory.shops:
                print(f"  Цех: {shop.name}, Работники: {shop.count_workers()}")

        elif choice == '7':
            break

        else:
            print("Некорректный выбор или завод не создан.")


if __name__ == "__main__":
    menu()
