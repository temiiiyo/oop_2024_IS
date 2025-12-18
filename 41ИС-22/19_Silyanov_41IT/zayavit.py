class Zayavit:
    def __init__(self, id, name, adres):
        self.id = id
        self.name = name
        self.adres = adres

    def __str__(self):
        return f"Заявитель(id={self.id}, имя={self.name}, адрес={self.adres})"

    def sozdaet(self, opisanie):
        from zayavka import Zayavka
        return Zayavka(id=None, zayavit=self, opisanie=opisanie)