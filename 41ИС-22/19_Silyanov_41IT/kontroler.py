class Kontroler:
    def proveryaet(self, zayavka):
        if zayavka.remont:
            print(f"Ремонт по заявке {zayavka.id} проверен и завершен.")
        else:
            print(f"Ремонт по заявке {zayavka.id} еще не выполнен.")