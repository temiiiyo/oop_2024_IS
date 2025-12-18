class Item:
    __ident = 0

    def __new__(cls, *args, **kwargs):
        cls.__ident += 1
        return super().__new__(cls)

    def __init__(self, name: str, price: int):
        self.__item_id = self.__ident
        self.__name = name
        self.__price = price

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, item_id):
        self.__item_id = item_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price