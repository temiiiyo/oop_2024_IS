from collections import deque
from visitor import Visitor

class Wardrobe:
    def __init__(self):
        self.queue = deque()

    def __str__(self):
        return f"Wardrobe(queue={list(self.queue)})"

    def __len__(self):
        return len(self.queue)

    def __add__(self, other):
        if isinstance(other, Visitor):
            self.queue.append(other)
        return self

    def add_visitor(self, visitor):
        self.queue.append(visitor)

    def remove_visitor(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, dress_number = line.strip().split(';')
                visitor = Visitor(int(id), name, int(dress_number))
                self.queue.append(visitor)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for visitor in self.queue:
                file.write(f"{visitor.id};{visitor.name};{visitor.dress_number}\n")