from Division import Division
from Factory import Factory
from Workshop import Workshop
from Worker import Worker
from WorkshopManager import WorkshopManager
from SectionManager import SectionManager

def read_from_file(file_path):
    divisions = {}
    current_division = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Division:"):
                _, division_type, division_name = line.split(maxsplit=2)
                if division_type == "Factory":
                    current_division = Factory(division_name)
                elif division_type == "Workshop":
                    current_division = Workshop(division_name)
                else:
                    raise ValueError(f"Неизвестный тип подразделения: {division_type}")
                divisions[division_name] = current_division

            elif line.startswith("Employee:"):
                _, employee_type, employee_name = line.split(maxsplit=2)
                if current_division is None:
                    raise ValueError("Сотрудник указан вне подразделения!")

                if employee_type == "Worker":
                    employee = Worker(employee_name)
                elif employee_type == "WorkshopManager":
                    employee = WorkshopManager(employee_name)
                elif employee_type == "SectionManager":
                    employee = SectionManager(employee_name)
                else:
                    raise ValueError(f"Неизвестный тип сотрудника: {employee_type}")

                current_division.add_employee(employee)

    return divisions

def write_to_file(file_path, divisions):
    with open(file_path, 'w', encoding='utf-8') as file:
        for division_name, division in divisions.items():
            file.write(str(division) + "\n")
            for employee in division.employees:
                file.write(f"  - {employee}\n")

input_file_path = "in.txt"
output_file_path = "out.txt"

divisions = read_from_file(input_file_path)
write_to_file(output_file_path, divisions)

print(f"Данные успешно записаны в файл {output_file_path}.")