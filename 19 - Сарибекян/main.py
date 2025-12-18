from applicant import Applicant
from request import Request
from database import Database  # Добавляем импорт базы данных
from report import Report  # Импортируем класс Report из отдельного файла


def load_applicants(file_path):
    applicants = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            id_, name, contact_info = line.strip().split(', ')
            applicants[int(id_)] = Applicant(name, contact_info)
    return applicants


def load_requests(file_path, applicants):
    requests = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            id_, applicant_id, description, status, executor, repair = line.strip().split(', ')
            applicant = applicants.get(int(applicant_id))
            if applicant:
                # Создаем Request с правильным ID
                request = Request(applicant, description, status, executor, repair)
                request.id = int(id_)  # Устанавливаем ID из файла
                requests.append(request)
    return requests


if __name__ == "__main__":
    # Вариант 1: Использование текстовых файлов (старый подход)
    applicants = load_applicants('applicants.txt')
    requests = load_requests('requests.txt', applicants)

    # Фильтруем неотработанные заявки
    unprocessed_requests = [request for request in requests if request.status == 'ожидает']

    print(f"Найдено неотработанных заявок: {len(unprocessed_requests)}")

    # Генерируем отчет из объектов
    Report.generate_report_from_objects(unprocessed_requests)

    print("\n" + "=" * 50)
    print("ВАЖНО: Это старый подход без базы данных")
    print("=" * 50)

    # Вариант 2: Использование базы данных (новый подход - РЕКОМЕНДУЕТСЯ)
    print("\n\nИспользование базы данных SQLite:")
    print("-" * 40)

    db = Database()

    # Загружаем данные в базу
    for applicant_id, applicant in load_applicants('applicants.txt').items():
        db.add_applicant(applicant.name, applicant.contact_info)

    # Генерируем отчет из базы данных
    Report.generate_report_from_db(db)

    db.close()