# order_status.py
"""Модуль с перечислением статусов заказа."""
class OrderStatus:
    """Перечисление статусов заказа."""
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

if __name__ == "__main__":
    print(f"Статус заказа: {OrderStatus.PENDING}")