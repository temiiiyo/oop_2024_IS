class Street:
    def __init__(self, id_street, name):
        self.id_street = id_street
        self.name = name

    def __str__(self):
        return f"Улица {self.name}, (ID: {self.id_street})"