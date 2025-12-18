class Account:
    def __init__(self, code, number, street_code, house, building, apartment, full_name):
        self.code = code
        self.number = number
        self.street_code = street_code
        self.house = house
        self.building = building
        self.apartment = apartment
        self.full_name = full_name

    def __str__(self):
        return f'{self.code} {self.number} {self.street_code} {self.house} {self.building} {self.full_name}'