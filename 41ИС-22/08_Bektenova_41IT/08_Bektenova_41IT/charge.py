class Charge:
    def __init__(self, code, account_code, service_code, quantity):
        self.code = code  # Код начисления
        self.account_code = account_code  # Код счета
        self.service_code = service_code  # Код услуги
        self.quantity = quantity  # Количество