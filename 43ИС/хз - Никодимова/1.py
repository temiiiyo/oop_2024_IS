import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# Функция для сериализации объекта Person в JSON
def save_to_json(person, filename):
    person_dict = {
        'name': person.name,
        'age': person.age
    }

    with open(filename, 'w') as f:
        json.dump(person_dict, f)  # Сериализация объекта в JSON


# Функция для десериализации данных из файла JSON
def load_from_json(filename):
    with open(filename, 'r') as f:
        person_dict = json.load(f)  # Десериализация данных из JSON

    return Person(name=person_dict['name'], age=person_dict['age'])


if __name__ == "__main__":
    person = Person("Alice", 30)

    save_to_json(person, 'person.json')
    print(f"Сохранен объект: {person}")

    loaded_person = load_from_json('person.json')
    print(f"Загружен объект: {loaded_person}")
