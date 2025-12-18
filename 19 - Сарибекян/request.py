class Request:
    def __init__(self, applicant, description, status='ожидает', executor=None, repair=None, id=None):
        self.id = id  # Добавляем поле ID
        self.applicant = applicant
        self.description = description
        self.status = status
        self.executor = executor
        self.repair = repair