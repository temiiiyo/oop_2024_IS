import openpyxl
import pandas as pd

def generate_excel_report(subject):
    exam_data = []
    try:
        with open(f"{subject.name}_exam_results.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ": " in line:
                    student_name, grade = line.strip().split(": ")
                    exam_data.append({"Student": student_name, "Grade": grade})
                else:
                    print(f"Некорректная строка в файле: {line.strip()}")

        if not exam_data:
            print("Нет данных для создания отчёта.")
            return

        df = pd.DataFrame(exam_data)
        excel_file = f"{subject.name}_exam_report.xlsx"
        df.to_excel(excel_file, index=False)
        print(f"Экзаменационная ведомость создана: {excel_file}")
    except FileNotFoundError:
        print(f"Файл с результатами экзамена для предмета {subject.name} не найден.")
    except Exception as e:
        print(f"Ошибка при генерации отчёта: {e}")