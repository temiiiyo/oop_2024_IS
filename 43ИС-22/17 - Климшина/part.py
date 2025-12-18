# part.py

class Part:
    def __init__(self, name: str, performance: int):
        self.name = name
        self.performance = performance

    def __str__(self):
        return f"{self.name}, производительность: {self.performance}"

class Processor(Part):
    def __init__(self, name: str, performance: int, frequency: int):
        super().__init__(name, performance)
        self.frequency = frequency

    def __str__(self):
        return f"{self.name}, частота: {self.frequency}MHz, производительность: {self.performance}"

class Motherboard(Part):
    def __init__(self, name: str, performance: int, chipset: str):
        super().__init__(name, performance)
        self.chipset = chipset

    def __str__(self):
        return f"{self.name}, чипсет: {self.chipset}, производительность: {self.performance}"

class Memory(Part):
    def __init__(self, name: str, performance: int, capacity: int):
        super().__init__(name, performance)
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}, объём: {self.capacity}GB, производительность: {self.performance}"
