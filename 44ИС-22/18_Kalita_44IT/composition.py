from carriage import Carriage
from diesel_locomotive import Locomotive
from place import Place


class Train:
    """Класс для представления состава."""

    def __init__(self, locomotive=None):
        self.locomotive = locomotive  # Тепловоз
        self.carriages = []  # Список вагонов

    @property
    def locomotive(self):
        return self._locomotive

    @locomotive.setter
    def locomotive(self, value):
        self._locomotive = value

    def add_carriage(self, carriage):
        """Добавление вагона в состав."""
        self.carriages.append(carriage)

    def remove_carriage(self, carriage):
        """Удаление вагона из состава."""
        self.carriages.remove(carriage)

    def __eq__(self, other):
        return (self.locomotive == other.locomotive and
                len(self.carriages) == len(other.carriages) and
                all(c1 == c2 for c1, c2 in zip(self.carriages, other.carriages)))

    def __len__(self):
        return len(self.carriages)

    def __str__(self):
        carriages_info = '\n'.join(str(carriage) for carriage in self.carriages)
        locomotive_info = str(self.locomotive) if self.locomotive else "Нет тепловоза"
        return (f"Состав:\n{locomotive_info}\n"
                f"Вагоны:\n{carriages_info if carriages_info else 'Нет вагонов'}")

    def save_to_file(self, filename):
        """Сохранение состояния состава в файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{self.locomotive.model},{self.locomotive.power}\n")  # Сохраняем тепловоз
            for carriage in self.carriages:
                file.write(f"{carriage.number},{carriage.carriage_type}\n")  # Сохраняем вагоны

    @classmethod
    def load_from_file(cls, filename):
        """Загрузка состояния состава из файла."""
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            locomotive_data = lines[0].strip().split(',')
            locomotive = Locomotive(locomotive_data[0], int(locomotive_data[1]))

            train = cls(locomotive)
            for line in lines[1:]:
                number, carriage_type = line.strip().split(',')
                train.add_carriage(Carriage(int(number), carriage_type))
            return train


if __name__ == '__main__':
    loaded_train = Train.load_from_file('train_data.txt')
    print("\nЗагруженный состав:")
    print(loaded_train)