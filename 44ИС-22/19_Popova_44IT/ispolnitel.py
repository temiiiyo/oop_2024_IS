class Ispolnitel: # Исполнитель
    def __init__(self, name, telefon):
        self.name = name
        self.telefon = telefon

    def __str__(self):
        return f"Исполнитель: {self.name}, Телефон: {self.telefon}"