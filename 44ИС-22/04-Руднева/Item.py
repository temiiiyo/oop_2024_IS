
class Item():
    """класс товар"""
    def __init__(self,id,name,price):
        self._id = id
        self.name = name
        self._price = price

    @property
    def id(self):
        """метод печати id"""
        print(self._id)

    @id.setter
    def id(self,x):
        """метод установки id"""
        if x>0 :
            self._id = x
        else:
            raise Exception("Неверное значение")

    @property
    def price(self):
        """метод получение цены"""
        print(self._price)
    @price.setter
    def price(self,x):
        """методж установки цены"""
        if x>0 :
            self._price = x
        else:
            raise Exception("Неверное значение")

    def __str__(self):
        """метод печати товара"""
        return (f"товаар №{self._id},название:{self.name},цена:{self._price}")

    def __eq__(self,other):
        """метод эквивалентности двух товаров"""
        if self.name == other.name and self.price == other.price:
            return True
        else:
            return False


if __name__ == "__main__":
    i = Item(1,'woda',100)
    i2 = Item(2,"woda",100)
    i3 = Item(3, "juice", 100)
    print(i)
    print(i.id)
    i.id = 2
    print(i)
    #i.id = -2
    print(i==i2)
    print(i==i3)