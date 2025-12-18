from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QDialog, QLabel, QLineEdit, QMessageBox
from Nakladnaya_class import Nakladnaya
import datetime
import openpyxl


class MainWindow(QMainWindow):
    def __init__(self, items_list):
        super().__init__()
        self.nacl_list = []
        self.items_list = items_list

        layout = QVBoxLayout()

        button_add_new_nacl = QPushButton('Добавить')
        button_add_new_nacl.clicked.connect(lambda x: self.add_new_nacl(self.items_list))

        button_excel = QPushButton('Excel')
        button_excel.clicked.connect(self.export_to_excel)

        layout.addWidget(button_add_new_nacl)
        layout.addWidget(button_excel)
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def export_to_excel(self):
        try:
            if not self.nacl_list:
                QMessageBox.warning(self, 'Ошибка', 'Накладная не создана')
                return

            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = f'{str(datetime.date.today())}'
            sheet.append(['Товар', 'Количество'])

            for nacl in self.nacl_list:
                for item_id, amount in nacl.items.items():
                    it_name = None
                    for item in self.items_list:
                        if item.item_id == item_id:
                            it_name = item.name
                            break
                    if it_name is None:
                        it_name = f"Товар #{item_id}"
                    sheet.append([it_name, str(amount)])

            file_path = f'{self.nacl_list[0].receiver}.xlsx'
            wb.save(file_path)
            QMessageBox.information(self, 'Успех', f'Накладная экспортирована в файл {file_path}')
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")
            QMessageBox.critical(self, 'Ошибка', f'Не удалось экспортировать накладную: {str(e)}')


    def add_new_nacl(self, it_list):
        def add_nacl():
            nonlocal dlg
            try:
                it_ids = list(map(int, items_to_nacl_label_le.text().split()))
                amounts = list(map(int, items__nacl_label_le.text().split()))

                if len(it_ids) != len(amounts):
                    QMessageBox.warning(dlg, 'Ошибка',
                                        'Количество ID товаров должно совпадать с количеством значений')
                    return

                items_dict = {}
                for item_id, amount in zip(it_ids, amounts):
                    if not any(item.item_id == item_id for item in self.items_list):
                        QMessageBox.warning(dlg, 'Ошибка',
                                            f'Товар с ID {item_id} не найден')
                        return
                    items_dict[item_id] = amount

                receiver = rec_le.text()
                if not receiver.strip():
                    QMessageBox.warning(dlg, 'Ошибка', 'Введите получателя')
                    return

                new_nacl = Nakladnaya(
                    date=datetime.date.today(),
                    receiver=receiver,
                    items=items_dict
                )
                self.nacl_list.append(new_nacl)
                QMessageBox.information(dlg, 'Успех', 'Накладная создана')
                dlg.close()

            except ValueError:
                QMessageBox.warning(dlg, 'Ошибка',
                                    'Введите числа в правильном формате')
            except Exception as e:
                QMessageBox.critical(dlg, 'Ошибка', f'Ошибка: {str(e)}')

        dlg = QDialog(self)
        dlg.setWindowTitle('Создание накладной')
        dlg.resize(400, 300)

        dlg_add_layout = QVBoxLayout()
        dlg.setLayout(dlg_add_layout)

        rec_label = QLabel('Введите получателя: ')
        rec_le = QLineEdit()

        items_text = ", ".join([f"{i.name} (ID: {i.item_id})" for i in it_list])
        items_label = QLabel(f'Товары в наличии: {items_text}')

        items_to_nacl_label = QLabel('Введите ID товаров для добавления в накладную (через пробел): ')
        items_to_nacl_label_le = QLineEdit()

        items__nacl_label = QLabel('Введите количество для каждого товара (через пробел): ')
        items__nacl_label_le = QLineEdit()

        button = QPushButton('Создать')
        button.clicked.connect(add_nacl)

        dlg_add_layout.addWidget(rec_label)
        dlg_add_layout.addWidget(rec_le)
        dlg_add_layout.addWidget(items_label)
        dlg_add_layout.addWidget(items_to_nacl_label)
        dlg_add_layout.addWidget(items_to_nacl_label_le)
        dlg_add_layout.addWidget(items__nacl_label)
        dlg_add_layout.addWidget(items__nacl_label_le)
        dlg_add_layout.addWidget(button)

        dlg.exec()