class AutoMobile:
    def __init__(self, brand, liscence, made, color):
        self.brand = brand
        self.liscence = liscence
        self.made = made
        self.color = color

    def __str__(self):  # метод объект класса в виде строки
        return f"Модель машины: {self.brand}, Лицензия:{self.liscence}, Производитель: {self.made}, Расцветка: {self.color}"


class Driver:
    def __init__(self, fio, age, num_liscence):
        self.fio = fio
        self.age = age
        self.num_liscence = num_liscence

    def get_info(self):
        return f"ФИО водителя: {self.fio}, возраст: {self.age}, номер лицензии: {self.num_liscence}"


class ParkPlace:
    def __init__(self, number, title_place):
        self.number = number
        self.title_place = title_place
        self.car = None

    def park(self, car):
        if not self.car:
            self.car = car
            return True
        return False

    def free(self):
        if self.car:
            self.car = None
            return True
        return False

    def __str__(self):  # метод объект класса в виде строки
        return f"Место {self.number}: {'Занято' if self.car else 'Свободно'}"


class AutoPark:
    def __init__(self):
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def park_car(self, car):
        for place in self.places:
            if place.park(car):
                return f"Машина припаркована: {place.number}"
        return "Нет доступных парковочных мест"

    def list_cars(self):
        parked_cars = [str(place.car) for place in self.places if place.car]
        return parked_cars if parked_cars else f"Нет припаркованных машин"

    def free_places(self):
        free_places = [str(place) for place in self.places if not place.car]
        return free_places if free_places else f"Нет свободных мест"

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Припаркованные машины:\n")
            for car in self.list_cars():
                f.write(car + '\n')
            f.write("\nСвободные места:\n")
            for place in self.free_places():
                f.write(place + '\n')


# пример
if __name__ == "__main__":
    auto_park = AutoPark()

    for i in range(1, 6):
        auto_park.add_place(ParkPlace(i, f"Место {i}"))

    car1 = AutoMobile("Тойота", "2167326", "Япония", "Красный")
    car2 = AutoMobile("Форд", "авыормаы", "США", "Синий")
    print(auto_park.park_car(car1))
    print(auto_park.park_car(car2))

    # список припаркованных машин
    print("Припаркованные машины:")
    for car in auto_park.list_cars():
        print(car)

    # свободные места
    print("Свободные места:")
    for place in auto_park.free_places():
        print(place)

    # Сохранение информации в файл
    auto_park.save_to_file("park_info.txt")
