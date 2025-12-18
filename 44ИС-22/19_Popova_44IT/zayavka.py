class Zayavka: # Заявка
    def __init__(self, zayavitel, opisanie, date):
        self.zayavitel = zayavitel
        self.opisanie = opisanie
        self.date = date
        self.ispolnitel = None