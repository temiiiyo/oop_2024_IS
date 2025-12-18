import openpyxl

def generate_excel_report(expenses_by_item, item_share, total_expenses):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Отчет"

    sheet.append(["Статья", "Сумма", "Доля (%)"])

    for item, expense in expenses_by_item.items():
        sheet.append([item, expense, f"{item_share[item]:.2f}"])

    sheet.append([])
    sheet.append(["Общий бюджет", total_expenses])
    
    wb.save("monthly_budget_report.xlsx")
