class Account:
    def __init__(self, id_acc, account_number, street, house, building, apartment, fio):
        self.id_acc = id_acc # код аккаунта
        self.account_number = account_number # номер лицевого счета
        self.street = street #улица
        self.house = house #дом
        self.building = building #корпус
        self.apartment = apartment #квартира
        self.fio = fio

    def __str__(self):
        return (f"Номер лицевого счета: {self.account_number} (Id {self.id_acc}), ФИО: {self.fio}"
                f"Адрес: ул. {self.street.name}, д. {self.house}, корпус {self.building}, кв. {self.apartment}")