# organisms/organism.py

class Organisms:
    def __init__(self, name, obitanie, diet):
        self.name = name
        self.obitanie = obitanie
        self.diet = diet

    def get_info(self):
        return f"имя: {self.name}, обитание: {self.obitanie}, вид: {self.diet}"

    def print_inheritance_tree(self):
        print(self.__class__.__name__)
        parent_class = self.__class__.__bases__[0]
        while parent_class:
            print(parent_class.__name__)
            parent_class = parent_class.__bases__[0] if parent_class.__bases__ else None
