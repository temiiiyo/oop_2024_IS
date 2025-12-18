class Garderob:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, visitor):
        if self.head is None:
            self.head = visitor
        elif self.tail is None:
            self.head.next_id = visitor
            self.tail = visitor
            self.tail.previous = self.head
        else:
            self.tail.next_id = visitor
            previous = self.tail
            self.tail = visitor
            self.tail.previous = previous


    def pop_up(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_id
            self.head.previous = None


    def delete(self, id):
        if self.head.id == id:
            self.head = self.head.next_id
            print(self.head.__getattribute__('name'))
            self.head.previous = None
        elif self.tail.id == id:
            self.tail = self.tail.previous
            self.tail.next_id = None
        else:
            current = self.head
            while True:
                if current.__getattribute__('id') == id:
                    current.previous.next_id = current.next_id
                if current == self.tail:
                    break
                current = current.next_id

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)