class Visitor:
    def __init__(self, id, name, dress_number):
        self.id = id
        self.name = name
        self.dress_number = dress_number

    def __str__(self):
        return f"Visitor(id={self.id}, name={self.name}, dress_number={self.dress_number})"

    def __eq__(self, other):
        if isinstance(other, Visitor):
            return self.id == other.id and self.name == other.name and self.dress_number == other.dress_number
        return False

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_dress_number(self):
        return self.dress_number

    def set_dress_number(self, dress_number):
        self.dress_number = dress_number