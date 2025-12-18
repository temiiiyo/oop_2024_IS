class Teplovoz:
    def __init__(self, number, power):
        self.number = number
        self.power = power

    def info(self):  # Исправлено на info
        return f'Тепловоз {self.number}, Мощность: {self.power} л.с.'