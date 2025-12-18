from abc import ABC, abstractmethod

# ==================================================
#               СТРАТЕГИИ СКИДОК
# ==================================================

class DiscountStrategy(ABC):
    """Абстрактная стратегия расчёта скидки"""

    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class FixedDiscount(DiscountStrategy):
    """Фиксированная скидка"""

    def __init__(self, discount: float):
        self.discount = discount

    def apply_discount(self, price: float) -> float:
        return max(price - self.discount, 0)


class PercentDiscount(DiscountStrategy):
    """Процентная скидка"""

    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.percent / 100)


# ==================================================
#                     МАГАЗИН
# ==================================================

class Shop:
    """Магазин C# товарами"""

    def __init__(self):
        self.products: list[float] = []

    def add_product(self, price: float):
        """Добавление товара"""
        self.products.append(price)

    def total_price(self) -> float:
        """Общая стоимость без скидки"""
        return sum(self.products)

    def total_with_discount(self, strategy: DiscountStrategy) -> float:
        """Стоимость C# учётом выбранной скидки"""
        return strategy.apply_discount(self.total_price())


# ==================================================
#                  ТОЧКА ВХОДА
# ==================================================

if __name__ == "__main__":

    # --- Покупатель ---
    buyer = Shop()
    buyer.add_product(100)
    buyer.add_product(200)
    buyer.add_product(50)

    print("💰 Стоимость без скидки:", buyer.total_price())

    # --- Фиксированная скидка ---
    fixed_discount = FixedDiscount(30)
    print("💸 Со скидкой 30 руб.:", buyer.total_with_discount(fixed_discount))

    # --- Процентная скидка ---
    percent_discount = PercentDiscount(10)
    print("📉 Со скидкой 10%:", buyer.total_with_discount(percent_discount))
