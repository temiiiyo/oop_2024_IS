from visitor import Visitor

class VisitorBuilder:
    def __init__(self):
        self.id = None
        self.name = None
        self.dress_number = None

    def set_id(self, id):
        self.id = id
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_dress_number(self, dress_number):
        self.dress_number = dress_number
        return self

    def build(self):
        return Visitor(self.id, self.name, self.dress_number)