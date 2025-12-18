import pandas as pd
class ServiceManager:
    def __init__(self):
        self.accounts = []  # Список лицевых счетов
        self.services = []  # Список услуг
        self.charges = []  # Список начислений
        self.streets = []  # Список улиц

    def add_account(self, account):
        self.accounts.append(account)

    def add_service(self, service):
        self.services.append(service)

    def add_charge(self, charge):
        self.charges.append(charge)

    def add_street(self, street):
        self.streets.append(street)

    def generate_invoice(self, account_number):
        # Поиск счета по номеру
        account = next((a for a in self.accounts if a.number == account_number), None)
        if not account:
            print(f"Счет с номером {account_number} не найден")
            print(f"Доступные счета: {[a.number for a in self.accounts]}")
            return None

        # Поиск начислений для этого счета
        account_charges = [c for c in self.charges if c.account_code == account.code]

        if not account_charges:
            print(f"Для счета {account_number} нет начислений")
            return None

        # Создаем DataFrame для извещения
        data = []
        total_amount = 0

        for charge in account_charges:
            # Находим услугу для этого начисления
            service = next((s for s in self.services if s.code == charge.service_code), None)
            if service:
                amount = charge.quantity * service.tariff
                total_amount += amount
                data.append({
                    'Услуга': service.name,
                    'Количество': charge.quantity,
                    'Тариф': service.tariff,
                    'Сумма': amount
                })

        # Добавляем итоговую сумму
        if data:
            df = pd.DataFrame(data)
            df.loc['Итого'] = ['', '', '', total_amount]
            return df
        return None

    def save_invoice_to_excel(self, invoice_df, filename):
        if invoice_df is not None:
            invoice_df.to_excel(filename, index=False)
            print(f"Извещение сохранено в {filename}")