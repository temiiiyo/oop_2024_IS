class Ispolnitel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Исполнитель(id={self.id}, имя={self.name})"

    def vypolnyaet(self, zayavka, opisanie_remonta, data_remonta):
        from remont import Remont
        zayavka.remont = Remont(id=None, opisanie=opisanie_remonta, data=data_remonta)