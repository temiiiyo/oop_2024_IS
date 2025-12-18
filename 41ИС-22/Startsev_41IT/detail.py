class Detail:
    def __init__(self, name: str, performance: int):
        self.name = name
        self.performance = performance

    def __str__(self):
        return f"{self.name} (Performance: {self.performance})"

class Processor(Detail):
    pass

class Motherboard(Detail):
    pass

class Memory(Detail):
    pass