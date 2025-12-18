class Locomotive:
    """Класс для представления тепловоза."""

    def __init__(self, model, power):
        self.model = model  # Модель тепловоза
        self.power = power  # Мощность тепловоза (л.с.)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    def __eq__(self, other):
        return (self.model == other.model and
                self.power == other.power)

    def __str__(self):
        return f"Тепловоз: {self.model}, Мощность: {self.power} л.с."

if __name__ == '__main__':
    locomotive = Locomotive("TEP70", 3000)
    print(locomotive)