import csv
from openpyxl import Workbook


class Worker:
    def __init__(self, name, dolshnost):
        self._name = name
        self._dolshnost = dolshnost

    @property
    def name(self):
        return self._name

    @property
    def dolshnost(self):
        return self._dolshnost

    @name.setter
    def name(self, value):
        self._name = value

    @dolshnost.setter
    def dolshnost(self, value):
        self._dolshnost = value

    def __str__(self):
        return f"{self.name} ({self.dolshnost})"


class Department:
    def __init__(self, name, count):
        self._name = name
        self._count = count

    @property
    def name(self):
        return self._name

    @property
    def count(self):
        return self._count

    @name.setter
    def name(self, value):
        self._name = value

    @count.setter
    def count(self, value):
        self._count = value

    def __str__(self):
        return f"{self.name} ({self.count})"


class Zex:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self.name


class Zavod:
    def __init__(self, worker, department, zex):
        self.worker = worker
        self.department = department
        self.zex = zex

    def __str__(self):
        return f"{self.worker.name} - {self.department.name} - {self.zex.name}"


class Otchet:
    def __init__(self, worker_file, department_file, zex_file, zavod_file):
        self.worker = self.load_worker(worker_file)
        self.department = self.load_department(department_file)
        self.zex = self.load_zex(zex_file)
        self.zavod = self.load_zavod(zavod_file)

    @staticmethod
    def load_worker(file_path):
        workers = {}
        with open(file_path, "r", encoding="utf-8") as file:
            # Читаем построчно, каждая строка - название должности
            lines = file.read().strip().split('\n')
            for i, line in enumerate(lines):
                if line.strip():  # Пропускаем пустые строки
                    # Создаем работника с уникальным именем
                    worker_name = f"Сотрудник_{i + 1}"
                    workers[worker_name] = Worker(worker_name, line.strip())
        return workers

    @staticmethod
    def load_department(file_path):
        departments = {}
        with open(file_path, "r", encoding="utf-8") as file:
            # Используем CSV или разбиваем по запятой
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:  # Проверяем, что есть достаточно элементов
                    departments[row[0]] = Department(row[0], int(row[1]))
        return departments

    @staticmethod
    def load_zex(file_path):
        zexes = {}
        with open(file_path, "r", encoding="utf-8") as file:
            # Читаем построчно
            lines = file.read().strip().split('\n')
            for i, line in enumerate(lines):
                if line.strip():
                    # Используем номер строки как ключ
                    zexes[str(i + 1)] = Zex(line.strip())
        return zexes

    def load_zavod(self, file_path):
        zavods = []
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split('\n')
            for i, line in enumerate(lines):
                if line.strip():
                    # Предполагаем формат: тип цеха
                    # Берем первого работника, первый отдел, первый цех
                    worker_key = list(self.worker.keys())[i % len(self.worker)] if self.worker else None
                    department_key = list(self.department.keys())[i % len(self.department)] if self.department else None
                    zex_key = list(self.zex.keys())[i % len(self.zex)] if self.zex else None

                    if worker_key and department_key and zex_key:
                        zavods.append(Zavod(
                            self.worker[worker_key],
                            self.department[department_key],
                            self.zex[zex_key]
                        ))
        return zavods

    def generate_report(self, output_file):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Отчет"
        sheet.append(["Должность работника", "Количество людей", "Цех"])

        for zavod in self.zavod:
            sheet.append([zavod.worker.dolshnost, zavod.department.count, zavod.zex.name])

        workbook.save(output_file)
        print(f"Отчет сохранен в файл {output_file}")


if __name__ == "__main__":
    otchet = Otchet(
        worker_file="worker.txt",
        department_file="department.txt",
        zex_file="zex.txt",
        zavod_file="zavod.txt"
    )

    otchet.generate_report("report.xlsx")