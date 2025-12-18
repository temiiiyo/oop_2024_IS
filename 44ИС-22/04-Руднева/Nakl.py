from Item import Item
class Nakladnaya():
    """класс накладная"""
    def __init__(self, id, data, polush, lst_items=[]):
        self.id = id
        self.data = data
        self.polush = polush
        self.lst_items = lst_items.copy()

    def add_item(self, item):
        """метод добавление нового товара"""
        self.lst_items.append(item)

    def __add__(self, other):
        """метод сложения двух накладных"""
        for it in other.lst_items:
            self.lst_items.append(it)


    def __len__(self):
        """метод определения размерности накладной"""
        return (len(self.lst_items))

    def __str__(self):
        """метод вывода/печати накладной"""
        line =''
        for item in self.lst_items:
            line += "\n" + str(item)
        return(f"накладная №{str(self.id)},получатель:{str(self.polush)},дата:{str(self.data)},товары:\n {str(line)}")



if __name__ == "__main__":

    n1 = Nakladnaya(1, '20-12-2024', 'Rudneva')
    n3 = Nakladnaya(2,'21-12-2024',"Koroleva")
    with open("in.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        id, name, price = line.strip().split(";")
        item = Item(id, name, price)
        n1.add_item(item)
    i = Item('5', 'woda', '100')
    #n3.add_item(i)
    print(len(n1))
    print(len(n3))
    #print(n3)
    n3.add_item(i)
    print(n3)
    print(n1)
    n1+=n3
    print(n1)

