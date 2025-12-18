from product import Product
from client import Client
from receptionist import WarrantyReceptionist
from technician import Technician
from manager import WarrantyManager
from excel_manager import ExcelManager

def main():
    print("Введите данные клиента")
    client_name = input("Имя клиента: ").strip()
    client = Client(name=client_name)

    print("\nВведите данные продукта:")
    product_name = input("Название продукта: ").strip()
    manufacturer = input("Производитель: ").strip()
    price = float(input("Цена продукта: "))
    warranty_period_days = int(input("Срок гарантии (в днях): "))
    product = Product(name=product_name, manufacturer=manufacturer, price=price, warranty_period_days=warranty_period_days)

    receptionist = WarrantyReceptionist(name="Ольга Петрова")
    technician = Technician(name="Алексей Смирнов")
    manager = WarrantyManager(name="Анна Кузнецова")
    excel_manager = ExcelManager()

    print("\nОбработка запроса...")
    reception_result = receptionist.accept_product(product, client)
    print(reception_result)

    if product.is_under_warranty():
        analysis_result = technician.analyze_product(product)
        print("Результат анализа:", analysis_result)

        decision = manager.make_decision(product, analysis_result)
        print("Решение начальника гарантийного отдела:", decision)

        if analysis_result["status"] == "repairable":
            excel_manager.add_repair(product, "ремонт", product.price * 0.2)
        elif analysis_result["status"] == "faulty":
            excel_manager.add_repair(product, "замена", product.price)
    else:
        print("Гарантия на продукт истекла.")

    repair_cost, replacement_cost = excel_manager.generate_report()
    print(f"Суммарные затраты на ремонт: {repair_cost}")
    print(f"Суммарные затраты на замену: {replacement_cost}")

    excel_manager.save()
    print("Данные сохранены в Excel-файл.")

if __name__ == "__main__":
    main()