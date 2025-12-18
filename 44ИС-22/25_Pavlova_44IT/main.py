from dispatcher import Dispatcher
from order import Order
from customer import Customer
from officeadministrator import OfficeAdministrator

class Main():
    def __init__(self):
        self.__init__(Order, Dispatcher, Customer, OfficeAdministrator)


if __name__ == "__main__":
    pass