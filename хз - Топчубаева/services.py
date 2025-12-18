class Service:
    def __init__(self, id_service, name, tarif):
        self.id_service = id_service
        self.name = name
        self.tarif = tarif

    def __str__(self):
        return (f"Услуга: {self.name}, (ID {self.id_service}), "
                f"Тариф: {self.tarif}")
