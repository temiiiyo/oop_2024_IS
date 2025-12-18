class Vagon:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def info(self):
        return f'Вагон {self.number}, Вместимость: {self.capacity}'

