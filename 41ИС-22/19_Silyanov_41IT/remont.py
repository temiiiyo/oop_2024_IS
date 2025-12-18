class Remont:
    def __init__(self, id, opisanie, data):
        self.id = id
        self.opisanie = opisanie
        self.data = data

    def __str__(self):
        return f"Ремонт(id={self.id}, описание={self.opisanie}, дата={self.data})"