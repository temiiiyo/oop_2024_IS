class Zayavka:
    def __init__(self, id, zayavit, opisanie, ispolnitel=None, remont=None):
        self.id = id
        self.zayavit = zayavit
        self.opisanie = opisanie
        self.ispolnitel = ispolnitel
        self.remont = remont

    def __str__(self):
        return (f"Заявка(id={self.id}, заявитель={self.zayavit.name}, "
                f"описание={self.opisanie}, исполнитель={self.ispolnitel}, "
                f"ремонт={self.remont})")

    def naznachaet(self, ispolnitel):
        self.ispolnitel = ispolnitel

    def utverzhdaet(self):
        print(f"Заявка {self.id} утверждена.")