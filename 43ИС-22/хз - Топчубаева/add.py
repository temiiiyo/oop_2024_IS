from services import Service
from streets import Street
from accounts import Account
from nachisleniya import Nachisleniya
from openpyxl import Workbook


class Manager:
        def __init__(self):
            self.accounts = []  # список лицевых счетов
            self.services = []  # список услуг
            self.streets = [] #список улиц
            self.nachisleniya = []  # список начислений

        def add_account(self, account):
            """добавление лицевого счета"""
            self.accounts.append(account)


        def add_service(self, service):
            """ добавление услуги"""
            self.services.append(service)

        def add_charge(self, nach):
            """добавление начисления"""
            self.nachisleniya.append(nach)

        def add_street(self, street):
            self.streets.append(street)


        def __add__(self, other):
            if not isinstance(other, Manager):
                raise TypeError("Можно складывать только объекты класса Manager.")

            # Создаем новый объект Manager
            new_manager = Manager()

            # Объединяем списки, исключая дубли
            new_manager.accounts = self.accounts + [acc for acc in other.accounts if acc not in self.accounts]
            new_manager.services = self.services + [srv for srv in other.services if srv not in self.services]
            new_manager.streets = self.streets + [strt for strt in other.streets if strt not in self.streets]
            new_manager.nachisleniya = self.nachisleniya + [nach for nach in other.nachisleniya if
                                                            nach not in self.nachisleniya]

            return new_manager

        def load_streets(self, f_name):
            with open(f_name, "r", encoding="utf-8") as file:
                for line in file:
                    id_street, name = line.strip().split(";")
                    self.add_street(Street(int(id_street), name))

        def load_accounts(self, f_name):
            with open(f_name, "r", encoding="utf-8") as file:
                for line in file:
                    id_acc, account_number, id_street, house, building, apartment, fio = line.strip().split(";")
                    street = next((s for s in self.streets if s.id_street == int(id_street)), None)
                    if street:
                        self.add_account(Account(int(id_acc), account_number, street, house, building, apartment, fio))

        def load_services(self, f_name):
            with open(f_name, "r", encoding="utf-8") as file:
                for line in file:
                    id_service, name, tarif = line.strip().split(";")
                    self.add_service(Service(int(id_service), name, float(tarif)))

        def load_charges(self, f_name):
            with open(f_name, "r", encoding="utf-8") as file:
                for line in file:
                    id_nach, account_number, id_service, quantity = line.strip().split(";")
                    account = next((a for a in self.accounts if a.account_number == account_number), None)
                    service = next((s for s in self.services if s.id_service == int(id_service)), None)

                    if account and service:
                        self.add_charge(Nachisleniya(int(id_nach), account, service, float(quantity)))
                    else:
                        if not account:
                            print(f"Счет с номером {account_number} не найден для начисления {id_nach}")
                        if not service:
                            print(f"Услуга с ID {id_service} не найдена для начисления {id_nach}")

        def generate_invoice(self, account_number):
            """поиск счета и начислений по номеру"""
            account = next((a for a in self.accounts if a.account_number == account_number), None)
            if not account:
                print(f"Счет с номером {account_number} не найден")
                return

            charges = [n for n in self.nachisleniya if n.account.account_number == str(account_number)]
            if not charges:
                print(f"Нет начислений для счета {account_number}")
                return

            wb = Workbook()
            ws = wb.active
            ws.title = "Извещение"

            ws.append(["ФИО", "Адрес", "Услуга", "Тариф", "Количество", "Итого"])
            total = 0
            for charge in charges:
                ws.append([
                    account.fio,
                    f"ул. {account.street.name}, д. {account.house}, корп. {account.building}, кв. {account.apartment}",
                    charge.service.name,
                    charge.service.tarif,
                    charge.quantity,
                    charge.calc_total()
                ])
                total += charge.calc_total()

            ws.append(["", "", "", "", "Итоговая сумма:", total])
            file_name = f"invoice_{account_number}.xlsx"
            wb.save(file_name)
            print(f"Извещение сохранено в файл {file_name}")





