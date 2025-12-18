from stack import Stack
from railCar import RailCar

class TrainSorter:

    def __init__(self):
        self.direction_a = Stack()
        self.direction_b = Stack()

    def sort_train(self, cars):
        for car in cars:
            if not RailCar.validate(car.car_type):
                print(f"Пропущен неверный тип вагона: {car.car_type}")
                continue
            if car.car_type == "грузовой":
                self.direction_a.push(car)
            elif car.car_type == "пассажирский":
                self.direction_b.push(car)

    def __str__(self):
        return (f"Направление A: {self.direction_a}\n"
                f"Направление B: {self.direction_b}")