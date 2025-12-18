from collections import defaultdict

# Расчет месячного бюджета и доли каждой статьи
def calculate_monthly_budget(expenses):
    total_expenses = 0
    expenses_by_item = defaultdict(float)

    for date, quantity, price, cost_item, category_name in expenses:
        expense = float(quantity) * float(price)
        total_expenses += expense
        expenses_by_item[cost_item] += expense
    
    item_share = {item: expense / total_expenses * 100 for item, expense in expenses_by_item.items()}
    
    return total_expenses, expenses_by_item, item_share

class BudgetComparisonError(Exception):
    """Исключение для ошибок при сравнении бюджета."""
    pass

