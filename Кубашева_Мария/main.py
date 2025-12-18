import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QMessageBox
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
import matplotlib.pyplot as plt


class WarrantyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Гарантийная мастерская")
        self.setGeometry(100, 100, 420, 600)
        self.setStyleSheet("""
            background-color: #f1f1f1;
            color: #333;
            font-family: 'Arial', sans-serif;
        """)

        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="WarrantyService"
            )
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных: {str(err)}")
            sys.exit()

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        image_label = QLabel()
        pixmap = QPixmap("workshop.png")
        image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)

        self.unfinished_button = self.create_button("Показать невыполненные ремонты")
        self.unfinished_button.clicked.connect(self.show_unfinished_repairs)
        layout.addWidget(self.unfinished_button)

        self.diagram_button = self.create_button("Построить диаграмму сложных ремонтов")
        self.diagram_button.clicked.connect(self.build_complex_repairs_chart)
        layout.addWidget(self.diagram_button)

    def create_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        """)
        button.setFixedWidth(400)
        button.setFixedHeight(80)
        button.setFont(QFont('Arial', 14))
        button.setCursor(Qt.CursorShape.PointingHandCursor)

        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        return button

    def show_unfinished_repairs(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT EquipmentName, RequestDate FROM Repairs WHERE CompletionDate IS NULL"
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                message = "Невыполненные ремонты:\n"
                for row in results:
                    message += f"{row[0]} (Дата обращения: {row[1]})\n"
                QMessageBox.information(self, "Невыполненные ремонты", message)
            else:
                QMessageBox.information(self, "Невыполненные ремонты", "Все ремонты завершены.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {str(err)}")

    def build_complex_repairs_chart(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT m.Name, COUNT(r.RepairID) AS RepairCount 
                FROM Repairs r
                JOIN RepairCategories c ON r.CategoryID = c.CategoryID
                JOIN EquipmentTypes e ON r.EquipmentTypeID = e.EquipmentTypeID
                JOIN Manufacturers m ON e.ManufacturerID = m.ManufacturerID
                WHERE c.Name = 'Сложный'
                GROUP BY m.Name
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                manufacturers = [row[0] for row in results]
                repair_counts = [row[1] for row in results]


                plt.figure(figsize=(10, 6))
                plt.bar(manufacturers, repair_counts, color='skyblue')
                plt.title('Количество сложных ремонтов по производителям', fontsize=18, fontweight='bold')
                plt.xlabel('Производитель', fontsize=14)
                plt.ylabel('Количество ремонтов', fontsize=14)
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.show()
            else:
                QMessageBox.information(self, "Диаграмма", "Нет данных для построения диаграммы.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму: {str(err)}")

    def closeEvent(self, event):
        self.connection.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarrantyApp()
    window.show()
    sys.exit(app.exec())
