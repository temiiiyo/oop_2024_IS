import sys
from PyQt6.QtWidgets import QApplication
from gui import BudgetApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BudgetApp()
    window.show()
    sys.exit(app.exec())