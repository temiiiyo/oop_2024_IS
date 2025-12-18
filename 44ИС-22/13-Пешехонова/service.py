class Service:
    def __init__(self, code, name, tariff):
        self.code = code
        self.name = name
        self.tariff = tariff
    def __str__(self):
        return f'{self.code} {self.name} {self.tariff}'