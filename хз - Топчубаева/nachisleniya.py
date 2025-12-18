class Nachisleniya:
    def __init__(self, id_nach, account, service, quantity):
        self.id_nach = id_nach
        self.account = account
        self.service = service
        self.quantity = quantity

    def calc_total(self):
        return self.quantity * self.service.tarif

    def __str__(self):
        return (f"Начисление {self.id_nach} (Счет: {self.account.account_number}, "
                f"Услуга: {self.service.name}, Количество: {self.quantity}, "
                f"Итого {self.calc_total()}")