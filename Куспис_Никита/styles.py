#Стиль для приложения
MAIN_WINDOW_STYLE = """
    QMainWindow {
        background-color: #F5E1C0;
    }
    QLabel {
        font: bold 20px;
        color: #B32D00;
    }
    QPushButton {
        background-color: rgba(179, 45, 0, 180);
        border: 2px solid #B32D00;
        color: white;
        font-size: 14px;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: rgba(179, 45, 0, 255);
    }
    QTableWidget {
        background-color: #F8D7B6;
        border: 1px solid #B32D00;
        color: black;
    }
    QDialog {
        background-color: #F5E1C0;
    }
    QLineEdit {
        background-color: #F5E1C0;
        border: 2px solid #B32D00;
        padding: 5px;
        color: #B32D00;
        font: bold 18px;
    }
    QLineEdit:focus {
        border: 2px solid #B32D00;
    }
"""
