from car import Car
from driver import Driver
from parking_space import ParkingSpace
from parking_log import ParkingLot

def read_cars(file_path: str):
    cars = []
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 4:
                    print(f"Некорректная строка в файле {file_path}: {line.strip()}")
                    continue
                license_plate, mark, model, year_str = parts
                try:
                    year = int(year_str)
                except ValueError:
                    print(f"Некорректный год: {year_str} в строке: {line.strip()}")
                    continue
                car = Car(license_plate, mark, model, year)
                cars.append(car)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    return cars

def read_drivers(file_path: str):
    drivers = []
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(maxsplit=1)
                if len(parts) < 2:
                    print(f"Некорректная строка в файле {file_path}: {line.strip()}")
                    continue
                name, license_number = parts
                driver = Driver(name, license_number)
                drivers.append(driver)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    return drivers

def main():
    # Чтение данных
    cars = read_cars("cars.txt")
    drivers = read_drivers("drivers.txt")

    if len(cars) != len(drivers):
        print("Внимание: количество автомобилей и водителей не совпадает.")
        min_len = min(len(cars), len(drivers))
        cars = cars[:min_len]
        drivers = drivers[:min_len]

    # Создаем парковку и добавляем места
    parking_lot = ParkingLot()
    parking_lot.add_space(ParkingSpace(1))
    parking_lot.add_space(ParkingSpace(2))
    parking_lot.add_space(ParkingSpace(3))

    # Паркуем автомобили
    for car, driver in zip(cars, drivers):
        parking_lot.park_car(car, driver)

    # Отображение текущего состояния парковки
    print("\nТекущий статус парковки:")
    parking_lot.show_status()

    # Удаление автомобиля по госномеру
    license_number_to_remove = "ABC123"  # Можно заменить или сделать ввод с клавиатуры
    print(f"\nПопытка убрать автомобиль с госномером {license_number_to_remove}:")
    success = parking_lot.remove_car(license_number_to_remove)
    if success:
        print("Автомобиль успешно убран.")
    else:
        print("Автомобиль не найден или уже убран.")

    # Еще раз показываем статус
    print("\nОбновленный статус парковки:")
    parking_lot.show_status()

if __name__ == "__main__":
    main()