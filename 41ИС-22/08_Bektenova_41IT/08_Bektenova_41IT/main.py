from service_manager import ServiceManager
from account import Account
from service import Service
from charge import Charge
from street import Street


def main():
    manager = ServiceManager()
    service1 = Service(1, "Водоснабжение", 100)
    service2 = Service(2, "Электроснабжение", 150)

    manager.add_service(service1)
    manager.add_service(service2)

    street1 = Street(1, "Ленина")
    manager.add_street(street1)

    account1 = Account(1, "001", 1, "12", "", "45", "Иванов Иван Иванович")
    account2 = Account(2, "002", 1, "12", "", "46", "Петров Петр Петрович")

    manager.add_account(account1)
    manager.add_account(account2)

    # Создаем начисления
    charge1 = Charge(1, 1, 1, 5)  # 5 кубов воды для счета с кодом 1
    charge2 = Charge(2, 1, 2, 10)  # 10 кВт электроэнергии для счета с кодом 1
    charge3 = Charge(3, 2, 1, 3)  # 3 куба воды для счета с кодом 2

    manager.add_charge(charge1)
    manager.add_charge(charge2)
    manager.add_charge(charge3)

    # Генерация извещения для лицевого счета 001
    invoice_df = manager.generate_invoice("001")

    if invoice_df is not None:
        print("Извещение для счета 001:")
        print(invoice_df)
        manager.save_invoice_to_excel(invoice_df, "invoice_001.xlsx")
    else:
        print("Счет не найден")


if __name__ == "__main__":
    main()

