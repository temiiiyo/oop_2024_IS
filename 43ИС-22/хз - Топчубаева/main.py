from streets import Street
from accounts import Account
from services import Service
from nachisleniya import Nachisleniya
from add import Manager



def main():
    manager = Manager()
    manager2 = Manager()
    combined_manager = None

    manager.load_streets("street.txt")
    manager.load_accounts("accounts.txt")
    manager.load_services("services.txt")
    manager.load_charges("nachisleniya.txt")


    manager2.load_streets("streets2.txt")
    manager2.load_accounts("accounts2.txt")
    manager2.load_services("services2.txt")
    manager2.load_charges("nachisleniya2.txt")


    combined_manager = manager + manager2


    print("\nОбъединенные данные:")
    print("Список улиц:")
    for street in combined_manager.streets:
        print(street)

    print("\nСписок счетов:")
    for account in combined_manager.accounts:
        print(account)

    print("\nСписок услуг:")
    for service in combined_manager.services:
        print(service)

    print("\nСписок начислений:")
    for charge in combined_manager.nachisleniya:
        print(charge)

    while True:
        print("\nМеню:")
        print("1. Сформировать извещение для лицевого счета")
        print("2. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            account_number = input("Введите номер лицевого счета: ")
            try:
                manager.generate_invoice(account_number)
            except Exception as e:
                print(f"Ошибка при генерации извещения: {e}")
        elif choice == "2":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")




if __name__ == "__main__":
    main()