# Класс цехов
class Shop:
    def __init__(self, name: str):
        self._name = name
        self._sections = []  # Список участков

    @property
    def name(self):
        return self._name

    """добавление """
    def add_section(self, section):
        self._sections.append(section)
        print(f"Участок {section.name} добавлен в цех {self.name}.")

    def __str__(self):
        return f"Shop(Name: {self.name}, Sections: {len(self._sections)})"


if __name__ == "__main__":
    shop = Shop("Цех 1")
    print(shop)
