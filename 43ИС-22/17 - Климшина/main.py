# main.py

import pandas as pd
from part import Processor, Motherboard, Memory
from computer import Computer

def export_to_excel(computer: Computer, filename: str):
    data = {
        "Название": [part.name for part in computer.parts],
        "Производительность": [part.performance for part in computer.parts],
        "Полное Описание": [str(part) for part in computer.parts],  # Используем строковое представление для полного описания
    }
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Описание и состав компьютера сохранены в: {filename}")

def main():
    cpu = Processor("Intel i7", 3200, 3600)
    motherboard = Motherboard("Asus B450", 500, "B450")
    ram = Memory("Corsair 16GB", 1600, 16)

    computer = Computer()
    computer.add_part(cpu)
    computer.add_part(motherboard)
    computer.add_part(ram)

    print("Состав компьютера:")
    print(computer)

    new_cpu = Processor("Intel i9", 3800, 3800)
    computer.upgrade(cpu, new_cpu)

    print("\nСостав компьютера после модернизации:")
    print(computer)

    computer.repair(motherboard)

    another_computer = Computer()
    another_computer.add_part(Processor("AMD Ryzen 5", 3400, 3500))
    another_computer.add_part(Motherboard("MSI Tomahawk", 480, "B450"))
    another_computer.add_part(Memory("HyperX 8GB", 1600, 8))

    print("\nСравнение компьютеров:")
    comparison_result = "равны" if computer == another_computer else "не равны"
    print(f"Компьютеры {comparison_result} по производительности.")

    export_to_excel(computer, "composition.xlsx")

if __name__ == '__main__':
    main()