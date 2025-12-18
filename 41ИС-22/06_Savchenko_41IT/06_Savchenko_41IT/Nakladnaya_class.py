import datetime


class Nakladnaya:
    def __init__(self, date: datetime.date, receiver: str, items: dict):
        self.__date = date
        self.__receiver = receiver
        self.__items = items

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def receiver(self):
        return self.__receiver

    @receiver.setter
    def receiver(self, receiver):
        self.__receiver = receiver

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items