from zayavitel import Zayavitel
from zayavka import Zayavka
from ispolnitel import Ispolnitel
from remont import Remont

def main():
    # чтение данных
    zayavki = []
    with open('zayavki.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:
            values = line.strip().split('\t')
            zayavitel = Zayavitel(values[0], values[1])
            zayavka = Zayavka(zayavitel, values[2], values[3])
            ispolnitel = Ispolnitel(values[4], values[5])
            remont = Remont(values[6], values[7])

            if remont.opisanie == "Не отработано": # список заявок
                zayavki.append({
                    "Заявитель": str(zayavka.zayavitel),
                    "Описание": zayavka.opisanie,
                    "Дата заявки": zayavka.date,
                    "Исполнитель": str(ispolnitel),
                    "Дата ремонта": remont.date,
                    "Описание ремонта": remont.opisanie
                })

    # запись данных
    with open("otchet.txt", "w", encoding="utf-8") as file:
        if zayavki:
            headers = list(zayavki[0].keys())
            file.write("\t".join(headers) + "\n")

            for zayavka in zayavki:
                file.write("\t".join(str(value) for value in zayavka.values()) + "\n")

if __name__ == "__main__":
    main()