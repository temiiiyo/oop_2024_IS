class Shop:
    """Класс для цеха."""
    def __init__(self, name, chief):
        self.name = name
        self.chief = chief
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def __str__(self):
        return f"Цех: {self.name}, начальник: {self.chief.name}, рабочих: {len(self.workers)}"