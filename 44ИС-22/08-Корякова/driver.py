class Driver:
    def __init__(self, name: str, license_number: str):
        self._name = name
        self._license_number = license_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def __str__(self):
        return f"{self._name} (Гос.номер: {self._license_number})"

    def __eq__(self, other):
        if isinstance(other, Driver):
            return self._license_number == other._license_number
        return False

    @staticmethod
    def read_drivers(file_path: str):
        drivers = []
        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    name = ' '.join(parts[:-1])  # все кроме последнего
                    license_number = parts[-1]
                    driver = Driver(name, license_number)
                    drivers.append(driver)
                else:
                    print(f"Некорректная строка: {line.strip()}")
        return drivers

if __name__ == "__main__":
    file_path = "drivers.txt"
    try:
        drivers = Driver.read_drivers(file_path)
        for driver in drivers:
            print(driver)
    except FileNotFoundError:
        print(f"Ошибка, файл '{file_path}' не найден.")
