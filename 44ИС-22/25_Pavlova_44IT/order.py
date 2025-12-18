class Order():
    def __init__(self, order_id, customer, specification, price, planned_delivery_date):
        self.order_id = order_id
        self.customer = customer
        self.specification = specification
        self.price = price
        self.planned_delivery_date = planned_delivery_date
        self.status = "Новый"
    @property
    def order_id(self):
        return self.order_id
    @property
    def customer(self):
        return self.customer
    @property
    def specification(self):
        return self.specification
    @property
    def price(self):
        return self.price
    @property
    def planned_delivery_date(self):
        return self.planned_delivery_date

    @order_id.setter
    def order_id(self, value):
        self.order_id = value


    def __len__(self):
        return len(self.price)

    def __eq__(self, other):
        return(self.order_id == other.order_id and self.customer == other.customer and self.specification == other.specification and self.price == other.price and self.planned_delivery_date == other.planned_delivery_date)

    def get_mebel(filename):
        '''считывание мебели из файла'''
        with open(filename, "r") as file:
            for line in file:
                order_id, customer, specification, price, planned_delivery_date = line.strip().split(", ")

            print(f"Id: {order_id}\nПокупатель: {customer}\nСпецификация: {specification}\nЦена: {price}\nОжидаемая дата доставки: {planned_delivery_date}")

    @classmethod
    def update_status(cls, new_status):
        cls.status = new_status
        print(f"Статус заказа {cls.order_id} изменен на '{new_status}'.")

    def __str__(self):
        return f"ID: {self.order_id}, покупатель: {self.customer}, спецификация: {self.specification}, цена: {self.price}, ожидаемая дата: {self.planned_delivery_date}, статус: {self.status}"

if __name__ == "__main__":
    filename = "order.txt"
    Order.get_mebel(filename)