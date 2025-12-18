from animal_species import AnimalSpecies

def parse_animals(input_file):
    """
    Чтение данных из текстового файла и создание объектов животных.

    Args:
        input_file (str): Путь к входному файлу.

    Returns:
        list: Список объектов AnimalSpecies.
    """
    animals = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            data = {key.strip(): value.strip() for key, value in
                    (pair.split(":") for pair in line.split(", "))}
            animal = AnimalSpecies(
                species_name=data["Вид"],
                genus_name=data["Род"],
                family_name=data["Семейство"],
                order_name=data["Отряд"],
                class_name=data["Класс"],
                animal_type=data["Тип"],
            )
            animals.append(animal)
    return animals

def find_animal_by_species(animals, species_name):
    """
    Поиск животного по его виду.

    Args:
        animals (list): Список объектов AnimalSpecies.
        species_name (str): Название вида для поиска.

    Returns:
        AnimalSpecies: Найденный объект животного или None.
    """
    for animal in animals:
        if animal.species_name.lower() == species_name.lower():
            return animal
    return None


def save_animal_to_file(animal, output_file):
    """
    Запись информации о найденном животном в выходной файл.

    Args:
        animal (AnimalSpecies): Объект животного для записи.
        output_file (str): Путь к выходному файлу.
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(animal) + "\n")


if __name__ == "__main__":
    input_file = "animals.txt"
    output_file = "selected_animal.txt"

    try:
        animals = parse_animals(input_file)
        print(f"Успешно загружено {len(animals)} записи(-ей).")
    except FileNotFoundError:
        print(f"Ошибка: входной файл '{input_file}' не найден.")
        exit(1)

    species_name = input("Введите название вида животного для поиска: ").strip()
    found_animal = find_animal_by_species(animals, species_name)

    if found_animal:
        print(f"\nНайдено животное:\n{found_animal}\n")
        save_animal_to_file(found_animal, output_file)
        print(f"\nИнформация записана в файл '{output_file}'.")
    else:
        print(f"Животное с видом '{species_name}' не найдено.")