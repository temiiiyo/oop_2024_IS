# computer.py

from typing import List
from part import Part

class Computer:
    def __init__(self):
        self.parts: List[Part] = []

    def add_part(self, part: Part):
        self.parts.append(part)
        print(f"Добавлена деталь: {part}")

    def upgrade(self, old_part: Part, new_part: Part):
        if old_part in self.parts:
            self.parts.remove(old_part)
            self.parts.append(new_part)
            print(f"Произведена замена {old_part} на {new_part}")

    def repair(self, part: Part):
        if part in self.parts:
            print(f"Деталь {part.name} отремонтирована.")

    def total_performance(self):
        return sum(part.performance for part in self.parts)

    def __str__(self):
        return "\n".join(str(part) for part in self.parts)

    def __eq__(self, other):
        if not isinstance(other, Computer):
            return False
        return self.total_performance() == other.total_performance()

    def __lt__(self, other):
        return self.total_performance() < other.total_performance()