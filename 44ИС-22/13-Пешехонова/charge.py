class Charge:
    def __init__(self, code, account_code, service_code, amount):
        self.code = code
        self.account_code = account_code
        self.service_code = service_code
        self.amount = amount
    def __str__(self):
        return f'{self.code} {self.account_code} {self.service_code} {self.amount}'