from Item_class import Item
from MainWindow_class import MainWindow, QApplication
import sys

item1 = Item('Игрушка1', 2300)
item2 = Item('Игрушка2', 2500)
item3 = Item('Игрушка3', 2000)
items_list = [item1, item2, item3]

app = QApplication(sys.argv)
window = MainWindow(items_list)
window.show()
sys.exit(app.exec())