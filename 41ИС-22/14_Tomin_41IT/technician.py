class Technician:
    def __init__(self, name):
        self.name = name

    def analyze_product(self, product):
        print(f"Мастер {self.name} анализирует продукт...")
        status = input("Введите статус анализа (faulty/repairable/ok): ").strip()
        description = input("Введите описание проблемы: ").strip()
        return {"status": status, "description": description}