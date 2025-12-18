from PyQt6.QtWidgets import *
import mysql.connector
from config import *
from workers.worker import *
from product import Product
from workers.boss import *
from workers.rabochiy import *

Worker1 = Boss("Ilia", "123123", "Аналитика", 120000)
Worker2 = Rabochiy("Sergey", "321321", 20000)

print(f"{Worker1.name} (Босс):")
print(f"  Зарплата до повышения: {Worker1.salary} руб.")
Worker1.get_up()
print(f"  Зарплата после повышения: {Worker1.salary} руб.")

print(f"{Worker2.name} (Рабочий):")
print(f"  Зарплата до изменения: {Worker2.salary} руб.")
Worker2.get_up()
print(f"  Зарплата после повышения: {Worker2.salary} руб.")
period = Worker2.get_work_period()
print(f"  Период работы: {period}")