from Admin import Admin
from  Item import Item
from Nakl import Nakladnaya
from Person import Person
if __name__ == "__main__":



    with open ("person.txt",'r') as file:
        line = file.read()
        surname,name,otch,inn = line.strip().split(";")
        p = Person(name,surname,otch,inn)

    with open("naklad.txt",'r') as file:
        line = file.read()

    data = input("Введите дату поставки")
    n = Nakladnaya(1,data,p)
    with open("in.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        id,name,price = line.strip().split(";")
        item = Item(id,name,price)
        n.add_item(item)

    with open("out.txt","w") as file:
        file.write(str(n))
    print(n)






