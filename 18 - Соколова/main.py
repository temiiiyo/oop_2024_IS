#Спроектировать классы, описывающих формирование железнодорожного состава:
#Место, Вагон, Тепловоз, Состав,. Построить диаграмму классов.
#Разработать программу для демонстрации системы классов. Переопределить методы сравнения мест(например, оба купейных, нижняя полка), вагонов и составов, добавления и удаленияв состав вагонов и тепловоза.
#Программа должна сформировать описание состава в Excel-файле. Данные хранить в текстовом файле.
#Соколов Е.А Студент группы 43ИС-21

from mesto import Mesto
from vagon import Vagon
from teplovoz import Teplovoz
from sostav import Sostav

if __name__ == "__main__":
    # Создаем места
    # 257 мест для состава (например, 128 мест для первого вагона и 129 для второго)
    mesto1 = Mesto(1, "нижняя полка")
    mesto2 = Mesto(2, "верхняя полка")
    mesto3 = Mesto(3, "нижняя полка", True)

    # создаем вагон и добавляем в него места
    vagon1 = Vagon(101, "купейный")
    vagon1.add_mesto(mesto1)
    vagon1.add_mesto(mesto2)

    vagon2 = Vagon(102, "платформенный")
    vagon2.add_mesto(mesto3)

    # создаем тепловоз
    teplovoz = Teplovoz("ТЭП70", 3000)

    # Создаем состав
    sostav = Sostav()
    sostav.add_vagon(vagon1)
    sostav.add_vagon(vagon2)
    sostav.add_teplovoz(teplovoz)

    # отображаем состав
    print(sostav)

    # сохраняем состав в Excel
    sostav.save_to_excel("train_composition.xlsx")

