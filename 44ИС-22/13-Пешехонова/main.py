from street import Street
from account import Account
from service import Service
from charge import Charge

def load_streets(filename):
    streets = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            code, name = line.strip().split(',')
            streets.append(Street(int(code), name))
    return sorted(streets, key=lambda x: x.name)


def load_accounts(filename):
    accounts = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            accounts.append(Account(
                int(parts[0]), parts[1], int(parts[2]), parts[3], parts[4] or None, parts[5], parts[6]))
    return sorted(accounts, key=lambda x: x.number)


def load_services(filename):
    services = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            code, name, tariff = line.strip().split(',')
            services.append(Service(int(code), name, float(tariff)))
    return sorted(services, key=lambda x: x.name)


def load_charges(filename):
    charges = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            code, account_code, service_code, amount = line.strip().split(',')
            charges.append(Charge(int(code), int(account_code), int(service_code), float(amount)))
    return sorted(charges, key=lambda x: x.account_code)


streets = load_streets("streets.txt")
accounts = load_accounts("accounts.txt")
services = load_services("services.txt")
charges = load_charges("charges.txt")


def generate_invoice(account_number):
    account = next((a for a in accounts if a.number == account_number), None)
    if not account:
        print("Счет не найден")
        return

    account_charges = [c for c in charges if c.account_code == account.code]
    invoice = []
    invoice.append(f"Извещение на оплату: {account.full_name}")
    street = next((s.name for s in streets if s.code == account.street_code), "")
    invoice.append(f"Адрес: {street}, д.{account.house}, к. {account.building or '-'}, кв. {account.apartment}")
    invoice.append("\nНачисления:")
    total = 0
    for charge in account_charges:
        service = next((s for s in services if s.code == charge.service_code), None)
        if service:
            amount = service.tariff * charge.amount
            total += amount
            invoice.append(f"{service.name}: {charge.amount} × {service.tariff} = {amount:.2f}")
    invoice.append(f"\nИтого к оплате: {total:.2f}")
    filename = f"invoice_{account_number}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(invoice))
    print(f"Извещение сохранено в файл: {filename}")

generate_invoice("12345")