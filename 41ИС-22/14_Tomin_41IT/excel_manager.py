import openpyxl
from datetime import datetime

class ExcelManager:
    def __init__(self, filename="repair_report.xlsx"):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Отчет"
        self.sheet.append(["Дата", "Продукт", "Тип ремонта", "Стоимость"])

    def add_repair(self, product, repair_type, cost):
        self.sheet.append([datetime.now().strftime("%Y-%m-%d"), product.name, repair_type, cost])

    def generate_report(self):
        total_repair_cost = 0
        total_replacement_cost = 0
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            if row[2] == "ремонт":
                total_repair_cost += row[3]
            elif row[2] == "замена":
                total_replacement_cost += row[3]
        return total_repair_cost, total_replacement_cost

    def save(self):
        self.workbook.save(self.filename)