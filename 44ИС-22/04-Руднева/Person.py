class Person():
    """класс человек"""
    def __init__(self,name,surname,otch,inn):
        self.name = name
        self.surname = surname
        self.otch = otch
        self._inn = inn


    def __str__(self):
        """печать человека"""
        return(f"{self.surname} {self.name} {self.otch} ,ИНН:{self._inn}")

if __name__ == "__main__":
    p = Person('Анна','Руднева','Алексеевна',2134782)
    print(p)

