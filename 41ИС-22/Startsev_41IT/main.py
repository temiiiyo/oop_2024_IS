from detail import Processor, Motherboard, Memory
from computer import Computer
import pandas as pd

if __name__ == "__main__":
    cpu = Processor("Intel i5", 100)
    mb = Motherboard("ASUS", 80)
    ram = Memory("Corsair", 120)

    computer = Computer()
    computer.add_detail(cpu)
    computer.add_detail(mb)
    computer.add_detail(ram)

    print("Начальная конфигурация компьютера:")
    print(computer)

    new_cpu = Processor("Intel i7", 150)
    computer.upgrade(cpu, new_cpu)

    print("\nМодернизированная конфигурация компьютера:")
    print(computer)

    computer.repair(ram)

    print("\nОтремонтированная конфигурация компьютера:")
    print(computer)

    data = {
        "Detail": [detail.name for detail in computer.details],
        "Performance": [detail.performance for detail in computer.details]
    }

    df = pd.DataFrame(data)
    df.to_excel("computer_configuration.xlsx", index=False)
    print("\nКонфигурация компьютера была экспортирована")