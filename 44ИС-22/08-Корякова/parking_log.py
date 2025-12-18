from parking_space import ParkingSpace
from car import Car
from driver import Driver

class ParkingLot:
    def __init__(self):
        self.spaces = []

    def add_space(self, space: ParkingSpace):
        """Добавляет парковочное место."""
        self.spaces.append(space)

    def park_car(self, car: Car, driver: Driver):
        """Паркует автомобиль, если есть свободное место."""
        for space in self.spaces:
            if not space.is_occupied:
                if space.occupy(car):
                    log_entry = f"{driver} припаркован {car} в {space}\n"
                    self.log_movement(log_entry)
                    print(log_entry.strip())
                    return True
        print("Ошибка: Нет доступных парковочных мест.")
        return False

    def remove_car(self, license_plate: str):
        """Освобождает место, если найден автомобиль с указанным номером."""
        for space in self.spaces:
            if space.is_occupied and space.car.license_plate == license_plate:
                driver_info = f"Водитель с номером {license_plate} выехал из {space}\n"
                space.vacate()
                self.log_movement(driver_info)
                print(driver_info.strip())
                return True
        print("Ошибка: Автомобиль не найден.")
        return False

    def log_movement(self, entry: str):
        """Записывает перемещение в лог-файл."""
        with open("parking_log.txt", "a", encoding='utf-8') as log_file:
            log_file.write(entry)

    def show_status(self):
        """Показывает текущий статус парковки."""
        print("Текущий статус парковки:")
        for idx, space in enumerate(self.spaces, start=1):
            print(f"Место {idx}: {space}")

    def __len__(self):
        """Количество парковочных мест."""
        return len(self.spaces)

    def __add__(self, other):
        """Объединяет парковки или добавляет место."""
        if isinstance(other, ParkingSpace):
            self.spaces.append(other)
        elif isinstance(other, ParkingLot):
            self.spaces.extend(other.spaces)
        else:
            raise TypeError("Ожидается объект ParkingLot или ParkingSpace")
        return self

# Пример использования
if __name__ == "__main__":
    parking_lot1 = ParkingLot()
    parking_lot1.add_space(ParkingSpace(1))
    parking_lot1.add_space(ParkingSpace(3))

    parking_lot2 = ParkingLot()
    parking_lot2.add_space(ParkingSpace(2))
    parking_lot2.add_space(ParkingSpace(4))

    # Объединение двух парковок
    combined_parking_lot = parking_lot1 + parking_lot2
    print(f"Общее количество парковочных мест: {len(combined_parking_lot)}")
    combined_parking_lot.show_status()