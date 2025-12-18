class Visitor:
    def __init__(self, id, name, dress_number):
        self.id = id
        self.name = name
        self.dress_number = dress_number
        self.is_done = False

    def __getattr__(self, item):
        object.__getattribute__(item)
        return object