import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import MySQLdb
from MySQLdb import Error
import os
import sys


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MySQL Database Application")
        self.root.geometry("850x650")

        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'zak_db',
            'port': 3306,
            'charset': 'utf8mb4',
            'use_unicode': True,
            'autocommit': True
        }

        self.connection = None
        self.cursor = None

        self.create_widgets()

        self.root.after(500, self.auto_connect)

    def auto_connect(self):
        """Автоматическая попытка подключения при запуске"""
        try:
            self.connect_db()
        except:
            pass

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        connection_frame = ttk.LabelFrame(main_frame, text="Подключение к MySQL", padding="10")
        connection_frame.pack(fill=tk.X, pady=(0, 10))
        connection_frame.columnconfigure(1, weight=1)
        row = 0
        ttk.Label(connection_frame, text="Хост:").grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        self.host_entry = ttk.Entry(connection_frame, width=25)
        self.host_entry.grid(row=row, column=1, sticky=tk.EW, padx=5, pady=2)
        self.host_entry.insert(0, self.db_config['host'])
        row += 1
        ttk.Label(connection_frame, text="Пользователь:").grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        self.user_entry = ttk.Entry(connection_frame, width=25)
        self.user_entry.grid(row=row, column=1, sticky=tk.EW, padx=5, pady=2)
        self.user_entry.insert(0, self.db_config['user'])
        row += 1
        ttk.Label(connection_frame, text="Пароль:").grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        self.password_entry = ttk.Entry(connection_frame, width=25, show="*")
        self.password_entry.grid(row=row, column=1, sticky=tk.EW, padx=5, pady=2)
        self.password_entry.insert(0, self.db_config['password'])
        row += 1
        ttk.Label(connection_frame, text="База данных:").grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        self.database_entry = ttk.Entry(connection_frame, width=25)
        self.database_entry.grid(row=row, column=1, sticky=tk.EW, padx=5, pady=2)
        self.database_entry.insert(0, self.db_config['database'])
        row += 1
        ttk.Label(connection_frame, text="Порт:").grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        self.port_entry = ttk.Entry(connection_frame, width=25)
        self.port_entry.grid(row=row, column=1, sticky=tk.EW, padx=5, pady=2)
        self.port_entry.insert(0, str(self.db_config['port']))
        row += 1

        btn_frame = ttk.Frame(connection_frame)
        btn_frame.grid(row=row, column=0, columnspan=2, pady=10)

        self.connect_btn = ttk.Button(btn_frame, text="Подключиться", command=self.connect_db)
        self.connect_btn.pack(side=tk.LEFT, padx=5)

        self.disconnect_btn = ttk.Button(btn_frame, text="Отключиться", command=self.disconnect_db, state=tk.DISABLED)
        self.disconnect_btn.pack(side=tk.LEFT, padx=5)

        operations_frame = ttk.LabelFrame(main_frame, text="Операции с базой данных", padding="10")
        operations_frame.pack(fill=tk.X, pady=(0, 10))

        btn_frame2 = ttk.Frame(operations_frame)
        btn_frame2.pack()

        self.execute_btn = ttk.Button(btn_frame2, text="Показать все записи",
                                      command=self.execute_select, state=tk.DISABLED)
        self.execute_btn.pack(side=tk.LEFT, padx=5)

        self.add_btn = ttk.Button(btn_frame2, text="Добавить запись",
                                  command=self.show_add_dialog, state=tk.DISABLED)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.edit_btn = ttk.Button(btn_frame2, text="Редактировать",
                                   command=self.show_edit_dialog, state=tk.DISABLED)
        self.edit_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = ttk.Button(btn_frame2, text="Удалить запись",
                                     command=self.show_delete_dialog, state=tk.DISABLED)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ttk.Button(btn_frame2, text="Очистить",
                                    command=self.clear_output, state=tk.NORMAL)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        output_frame = ttk.LabelFrame(main_frame, text="Результаты", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True)

        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, font=("Consolas", 10))
        self.output_text.pack(fill=tk.BOTH, expand=True)

        self.status_bar = ttk.Label(self.root, text="Не подключено к базе данных",
                                    relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def update_db_config(self):
        """Обновление конфигурации из полей ввода"""
        self.db_config = {
            'host': self.host_entry.get(),
            'user': self.user_entry.get(),
            'password': self.password_entry.get(),
            'database': self.database_entry.get(),
            'port': int(self.port_entry.get()) if self.port_entry.get().isdigit() else 3306,
            'charset': 'utf8mb4',
            'use_unicode': True,
            'autocommit': True
        }

    def connect_db(self):
        """Подключение к базе данных MySQL"""
        try:
            self.update_db_config()
            if self.connection:
                self.disconnect_db()

            self.connection = MySQLdb.connect(**self.db_config)
            self.cursor = self.connection.cursor()

            self.connect_btn.config(state=tk.DISABLED)
            self.disconnect_btn.config(state=tk.NORMAL)
            self.execute_btn.config(state=tk.NORMAL)
            self.add_btn.config(state=tk.NORMAL)
            self.edit_btn.config(state=tk.NORMAL)
            self.delete_btn.config(state=tk.NORMAL)
            self.check_table_exists()

            self.output_text.insert(tk.END, f"✓ Подключено к MySQL\n")
            self.output_text.insert(tk.END, f"  Хост: {self.db_config['host']}\n")
            self.output_text.insert(tk.END, f"  База данных: {self.db_config['database']}\n")
            self.output_text.insert(tk.END, f"  Версия MySQL: {self.get_mysql_version()}\n\n")
            self.output_text.see(tk.END)

            self.status_bar.config(text=f"Подключено: {self.db_config['host']}/{self.db_config['database']}")

        except Error as e:
            error_msg = f"Ошибка подключения к MySQL:\n{str(e)}"
            messagebox.showerror("Ошибка подключения", error_msg)
            self.output_text.insert(tk.END, f"✗ Ошибка подключения: {str(e)}\n")
            self.output_text.see(tk.END)
        except Exception as e:
            error_msg = f"Неизвестная ошибка:\n{str(e)}"
            messagebox.showerror("Ошибка", error_msg)

    def disconnect_db(self):
        """Отключение от базы данных"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

            self.connection = None
            self.cursor = None

            self.connect_btn.config(state=tk.NORMAL)
            self.disconnect_btn.config(state=tk.DISABLED)
            self.execute_btn.config(state=tk.DISABLED)
            self.add_btn.config(state=tk.DISABLED)
            self.edit_btn.config(state=tk.DISABLED)
            self.delete_btn.config(state=tk.DISABLED)

            self.output_text.insert(tk.END, "✗ Отключено от базы данных\n\n")
            self.output_text.see(tk.END)
            self.status_bar.config(text="Не подключено к базе данных")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при отключении:\n{str(e)}")

    def get_mysql_version(self):
        """Получение версии MySQL сервера"""
        try:
            self.cursor.execute("SELECT VERSION()")
            version = self.cursor.fetchone()[0]
            return version
        except:
            return "Неизвестно"

    def check_table_exists(self):
        """Проверка существования таблицы Zak"""
        try:
            self.cursor.execute("""
                SELECT COUNT(*) 
                FROM information_schema.tables 
                WHERE table_schema = %s 
                AND table_name = 'Zak'
            """, (self.db_config['database'],))

            if self.cursor.fetchone()[0] == 0:
                self.output_text.insert(tk.END, "⚠ Таблица 'Zak' не существует. Создайте её в MySQL Workbench.\n")
                self.output_text.insert(tk.END, "SQL для создания:\n")
                self.output_text.insert(tk.END, """
CREATE TABLE Zak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    vRabote TINYINT(1) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
                """)
                self.output_text.see(tk.END)
                return False
            return True
        except:
            return False

    def execute_select(self, custom_query=None):
        """Выполнение SELECT запроса"""
        if not self.connection:
            messagebox.showwarning("Нет подключения", "Сначала подключитесь к базе данных")
            return

        try:
            if custom_query:
                query = custom_query
            else:
                query = "SELECT * FROM Zak ORDER BY id"

            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            self.clear_output()

            column_names = [desc[0] for desc in self.cursor.description]

            self.output_text.insert(tk.END, f"Запрос: {query}\n")
            self.output_text.insert(tk.END, f"Найдено записей: {len(rows)}\n")
            self.output_text.insert(tk.END, "=" * 60 + "\n\n")

            headers = " | ".join(str(name).ljust(15) for name in column_names)
            self.output_text.insert(tk.END, headers + "\n")
            self.output_text.insert(tk.END, "-" * len(headers) + "\n")

            for row in rows:
                formatted_row = " | ".join(str(value).ljust(15) for value in row)
                self.output_text.insert(tk.END, formatted_row + "\n")

            self.save_to_file(rows, column_names, query)

            self.status_bar.config(text=f"Найдено {len(rows)} записей")
            self.output_text.see(tk.END)

        except Error as e:
            messagebox.showerror("Ошибка запроса", f"Ошибка при выполнении запроса:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неизвестная ошибка:\n{str(e)}")

    def save_to_file(self, rows, column_names, query):
        """Сохранение результатов в файл"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="mysql_output.txt"
            )

            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Запрос: {query}\n")
                    f.write(f"Дата выполнения: {self.get_current_time()}\n")
                    f.write(f"Количество записей: {len(rows)}\n")
                    f.write("=" * 50 + "\n\n")
                    f.write("\t".join(column_names) + "\n")
                    f.write("-" * (len(column_names) * 15) + "\n")
                    for row in rows:
                        f.write("\t".join(map(str, row)) + "\n")

                self.output_text.insert(tk.END, f"\n✓ Результаты сохранены в: {filename}\n")
                self.output_text.see(tk.END)

        except Exception as e:
            messagebox.showerror("Ошибка записи", f"Не удалось сохранить в файл:\n{str(e)}")

    def show_add_dialog(self):
        """Диалог добавления новой записи"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить запись")
        dialog.geometry("400x200")
        dialog.transient(self.root)
        dialog.grab_set()

        ttk.Label(dialog, text="Название записи:").pack(pady=(20, 5))
        name_entry = ttk.Entry(dialog, width=40)
        name_entry.pack(pady=5)
        name_entry.focus_set()

        ttk.Label(dialog, text="В работе (1-да, 0-нет):").pack(pady=5)
        vrabote_entry = ttk.Entry(dialog, width=10)
        vrabote_entry.insert(0, "1")
        vrabote_entry.pack(pady=5)

        def add_record():
            name = name_entry.get().strip()
            vrabote = vrabote_entry.get().strip()

            if not name:
                messagebox.showwarning("Внимание", "Введите название записи")
                return

            try:
                vrabote_int = int(vrabote)
                if vrabote_int not in (0, 1):
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Внимание", "Значение 'В работе' должно быть 0 или 1")
                return

            try:
                self.cursor.execute(
                    "INSERT INTO Zak (name, vRabote) VALUES (%s, %s)",
                    (name, vrabote_int)
                )
                self.connection.commit()

                self.output_text.insert(tk.END, f"Добавлена запись: '{name}' (vRabote={vrabote_int})\n")
                self.output_text.see(tk.END)
                self.status_bar.config(text="Запись добавлена")

                dialog.destroy()
                self.execute_select()

            except Error as e:
                messagebox.showerror("Ошибка", f"Ошибка при добавлении записи:\n{str(e)}")

        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="Добавить", command=add_record).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        dialog.bind('<Return>', lambda e: add_record())

    def show_edit_dialog(self):
        """Диалог редактирования записи"""
        try:
            self.cursor.execute("SELECT id, name FROM Zak ORDER BY id")
            records = self.cursor.fetchall()

            if not records:
                messagebox.showinfo("Информация", "В таблице нет записей для редактирования")
                return

            dialog = tk.Toplevel(self.root)
            dialog.title("Редактировать запись")
            dialog.geometry("500x400")
            dialog.transient(self.root)
            dialog.grab_set()
            ttk.Label(dialog, text="Выберите запись для редактирования:",
                      font=("Arial", 10, "bold")).pack(pady=10)

            listbox = tk.Listbox(dialog, height=10, width=50)
            listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

            for record_id, name in records:
                listbox.insert(tk.END, f"ID: {record_id} - {name}")

            scrollbar = ttk.Scrollbar(dialog, orient=tk.VERTICAL)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            def edit_selected():
                selection = listbox.curselection()
                if not selection:
                    messagebox.showwarning("Внимание", "Выберите запись для редактирования")
                    return

                selected_index = selection[0]
                record_id = records[selected_index][0]

                self.cursor.execute("SELECT * FROM Zak WHERE id = %s", (record_id,))
                record = self.cursor.fetchone()

                self.edit_record_dialog(record_id, record)
                dialog.destroy()

            btn_frame = ttk.Frame(dialog)
            btn_frame.pack(pady=10)

            ttk.Button(btn_frame, text="Редактировать", command=edit_selected).pack(side=tk.LEFT, padx=5)
            ttk.Button(btn_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        except Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при получении списка записей:\n{str(e)}")

    def edit_record_dialog(self, record_id, record):
        """Диалог редактирования конкретной записи"""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Редактирование записи ID: {record_id}")
        dialog.geometry("400x250")
        dialog.transient(self.root)
        dialog.grab_set()

        ttk.Label(dialog, text=f"Редактирование записи ID: {record_id}",
                  font=("Arial", 10, "bold")).pack(pady=(15, 10))

        fields_frame = ttk.Frame(dialog)
        fields_frame.pack(pady=10, padx=20)

        ttk.Label(fields_frame, text="Название:").grid(row=0, column=0, sticky=tk.W, pady=5)
        name_entry = ttk.Entry(fields_frame, width=30)
        name_entry.grid(row=0, column=1, pady=5, padx=10)
        name_entry.insert(0, record[1])

        ttk.Label(fields_frame, text="В работе (1-да, 0-нет):").grid(row=1, column=0, sticky=tk.W, pady=5)
        vrabote_entry = ttk.Entry(fields_frame, width=10)
        vrabote_entry.grid(row=1, column=1, pady=5, padx=10)
        vrabote_entry.insert(0, str(record[2]))

        def save_changes():
            new_name = name_entry.get().strip()
            new_vrabote = vrabote_entry.get().strip()

            if not new_name:
                messagebox.showwarning("Внимание", "Введите название записи")
                return

            try:
                vrabote_int = int(new_vrabote)
                if vrabote_int not in (0, 1):
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Внимание", "Значение 'В работе' должно быть 0 или 1")
                return

            try:
                self.cursor.execute(
                    "UPDATE Zak SET name = %s, vRabote = %s WHERE id = %s",
                    (new_name, vrabote_int, record_id)
                )
                self.connection.commit()

                self.output_text.insert(tk.END,
                                        f"✓ Обновлена запись ID {record_id}: '{new_name}' (vRabote={vrabote_int})\n")
                self.output_text.see(tk.END)
                self.status_bar.config(text="Запись обновлена")

                dialog.destroy()
                self.execute_select()

            except Error as e:
                messagebox.showerror("Ошибка", f"Ошибка при обновлении записи:\n{str(e)}")

        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        dialog.bind('<Return>', lambda e: save_changes())

    def show_delete_dialog(self):
        """Диалог удаления записи"""
        try:
            self.cursor.execute("SELECT id, name FROM Zak ORDER BY id")
            records = self.cursor.fetchall()

            if not records:
                messagebox.showinfo("Информация", "В таблице нет записей для удаления")
                return

            dialog = tk.Toplevel(self.root)
            dialog.title("Удалить запись")
            dialog.geometry("500x400")
            dialog.transient(self.root)
            dialog.grab_set()

            ttk.Label(dialog, text="Выберите запись для удаления:",
                      font=("Arial", 10, "bold")).pack(pady=10)

            listbox = tk.Listbox(dialog, height=10, width=50)
            listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

            for record_id, name in records:
                listbox.insert(tk.END, f"ID: {record_id} - {name}")

            scrollbar = ttk.Scrollbar(dialog, orient=tk.VERTICAL)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            def delete_selected():
                selection = listbox.curselection()
                if not selection:
                    messagebox.showwarning("Внимание", "Выберите запись для удаления")
                    return

                selected_index = selection[0]
                record_id = records[selected_index][0]
                record_name = records[selected_index][1]

                if not messagebox.askyesno("Подтверждение",
                                           f"Вы уверены, что хотите удалить запись?\nID: {record_id}\nНазвание: {record_name}"):
                    return

                try:
                    self.cursor.execute("DELETE FROM Zak WHERE id = %s", (record_id,))
                    self.connection.commit()

                    self.output_text.insert(tk.END, f"✓ Удалена запись ID {record_id}: '{record_name}'\n")
                    self.output_text.see(tk.END)
                    self.status_bar.config(text="Запись удалена")

                    dialog.destroy()
                    self.execute_select()

                except Error as e:
                    messagebox.showerror("Ошибка", f"Ошибка при удалении записи:\n{str(e)}")

            btn_frame = ttk.Frame(dialog)
            btn_frame.pack(pady=10)

            ttk.Button(btn_frame, text="Удалить выбранное", command=delete_selected).pack(side=tk.LEFT, padx=5)
            ttk.Button(btn_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        except Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при получении списка записей:\n{str(e)}")

    def clear_output(self):
        """Очистка поля вывода"""
        self.output_text.delete(1.0, tk.END)

    def get_current_time(self):
        """Получение текущего времени"""
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __del__(self):
        """Закрытие соединения при завершении"""
        try:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
        except:
            pass


def main():
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()