import pandas as pd
from zayavit import Zayavit
from zayavka import Zayavka
from ispolnit import Ispolnitel
from remont import Remont
from kontroler import Kontroler

class Otchet:
    def __init__(self, zayavki):
        self.zayavki = zayavki

    def gen_otchet(self, file_name):
        try:
            neotrabotannye_zayavki = [z for z in self.zayavki if z.remont is None]
            df = pd.DataFrame([{
                "ID заявки": z.id,
                "Заявитель": z.zayavit.name,
                "Адрес": z.zayavit.adres,
                "Описание": z.opisanie,
                "Исполнитель": z.ispolnitel.name if z.ispolnitel else "Не назначен"
            } for z in neotrabotannye_zayavki])
            df.to_excel(file_name, index=False)
            print(f"Отчет успешно сохранен в файл {file_name}")
        except PermissionError:
            print(f"Ошибка: файл {file_name} недоступен для записи.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def main():
    zayavit1 = Zayavit(1, "Иван Иванов", "ул. Ленина, д. 10")
    zayavit2 = Zayavit(2, "Анна Смирнова", "ул. Пушкина, д. 5")

    zayavka1 = zayavit1.sozdaet("Проблема с водоснабжением")
    zayavka2 = zayavit2.sozdaet("Проблема с электричеством")

    manager = Ispolnitel(1, "Менеджер")
    zayavka1.naznachaet(manager)
    zayavka1.utverzhdaet()

    ispolnitel = Ispolnitel(2, "Петр Петров")
    ispolnitel.vypolnyaet(zayavka1, "Замена труб", "2023-10-01")

    kontroler = Kontroler()
    kontroler.proveryaet(zayavka1)
    kontroler.proveryaet(zayavka2)

    zayavki = [zayavka1, zayavka2]
    otchet = Otchet(zayavki)
    otchet.gen_otchet("неотработанные_заявки.xlsx")

if __name__ == "__main__":
    main()