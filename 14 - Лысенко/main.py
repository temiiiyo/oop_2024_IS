import datetime


# Класс стеллаж
class Stelaz:
    def __init__(self, kod, nomer, kol_vo_yacheek, dopus_timaya_massa):
        self.kod = kod
        self.nomer = nomer
        self.kol_vo_yacheek = kol_vo_yacheek
        self.dopus_timaya_massa = dopus_timaya_massa
        self.pozitsii = []

    # Функция добавления позиции
    def add_position(self, pozitsiya):
        self.pozitsii.append(pozitsiya)

    # Функция для вычисления свободных ячеек
    def get_free_cells(self):
        return self.kol_vo_yacheek - len(self.pozitsii)

    # Функция для вычисления заполнения ячеек в %
    def get_fill_percentage(self):
        total_mass = sum(p.mass for p in self.pozitsii)
        return (total_mass / self.dopus_timaya_massa) * 100 if self.dopus_timaya_massa > 0 else 0


# Класс груз
class Gruz:
    def __init__(self, kod_gruza, nazvanie):
        self.kod_gruza = kod_gruza
        self.nazvanie = nazvanie


# Класс позиция
class Pozitsiya:
    def __init__(self, kod_gruza, kod_stelazha, nomer_yacheiki, massa, data_ukladki):
        self.kod_gruza = kod_gruza
        self.kod_stelazha = kod_stelazha
        self.nomer_yacheiki = nomer_yacheiki
        self.mass = massa
        self.data_ukladki = data_ukladki


if __name__ == "__main__":
    # Читаем данные из файла
    with open("input.txt", "r") as file:
        # Чтение данных о стеллаже
        line = file.readline().strip()
        if line:
            kod, nomer, kol_vo_yacheek, dopus_timaya_massa = line.split(", ")
            stelazh1 = Stelaz(int(kod), nomer, int(kol_vo_yacheek), float(dopus_timaya_massa))

        # Чтение данных о грузах
        for line in file:
            line = line.strip()
            if line == "0":
                break

            kod_gruza, nazvanie, massa = line.split(", ")
            massa = float(massa)

            # Создаем экземпляр груза
            gruz = Gruz(kod_gruza, nazvanie)

            # Добавляем позицию на стеллаж
            if stelazh1.get_free_cells() > 0:
                nomer_yacheiki = stelazh1.kol_vo_yacheek - stelazh1.get_free_cells() + 1  # Номер следующей свободной ячейки
                pozitsiya = Pozitsiya(gruz.kod_gruza, stelazh1.kod, nomer_yacheiki, massa, datetime.datetime.now())
                stelazh1.add_position(pozitsiya)
                print(f"Позиция добавлена: {gruz.nazvanie} в ячейку {nomer_yacheiki}.")
            else:
                print("Нет свободных ячеек на стеллаже.")

    # Получаем данные и записываем в файл
    with open("output.txt", "w") as file:
        file.write(f"Стеллаж {stelazh1.nomer}:\n")
        file.write(f"Свободные ячейки: {stelazh1.get_free_cells()}\n")
        file.write(f"Заполнение (в %): {stelazh1.get_fill_percentage():.2f}%\n")

    print("Данные успешно записаны в output.txt")
