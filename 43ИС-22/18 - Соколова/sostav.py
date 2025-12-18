from vagon import Vagon
from teplovoz import Teplovoz
from excel_utils import save_to_excel

class Sostav:
    # Конструктор класса Sostav, инициализирует пустой список вагонов и тепловоз как None
    def __init__(self):
        self.vagons = []  # Список вагонов в составе
        self.teplovoz = None  # Тепловоз (изначально None, т.е. не задан)

    # Метод для добавления вагона в состав
    def add_vagon(self, vagon):
        self.vagons.append(vagon)  # Добавляем объект вагона в список

    # Метод для удаления вагона из состава
    def remove_vagon(self, vagon):
        if vagon in self.vagons:
            self.vagons.remove(vagon)  # Удаляем вагон, если он есть в списке

    # Метод для добавления тепловоза в состав
    def add_teplovoz(self, teplovoz):
        self.teplovoz = teplovoz  # Устанавливаем тепловоз для состава

    # Метод для удаления тепловоза из состава
    def remove_teplovoz(self):
        self.teplovoz = None  # Убираем тепловоз из состава (ставим None)

    # Метод для отображения информации о составе
    def __str__(self):
        vagons_str = "\n".join([str(vagon) for vagon in self.vagons])  # Строковое представление всех вагонов
        return f"Состав:\nТепловоз: {self.teplovoz}\nВагоны:\n{vagons_str}"  # Формируем итоговую строку о составе

    # Метод для сохранения состава в Excel
    def save_to_excel(self, filename="sostav.xlsx"):
        save_to_excel(self, filename)  # Используем функцию для сохранения в Excel

