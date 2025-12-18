class Account:
    def __init__(self, code, number, street_code, house, building, apartment, owner):
        self.code = code  # Код счета
        self.number = number  # Номер счета
        self.street_code = street_code  # Код улицы
        self.house = house  # Дом
        self.building = building  # Корпус
        self.apartment = apartment  # Квартира
        self.owner = owner  # Владелец