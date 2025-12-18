from detail import Detail

class Computer:
    def __init__(self):
        self.details = []

    def add_detail(self, detail: Detail):
        self.details.append(detail)

    def upgrade(self, detail: Detail, new_detail: Detail):
        for i, d in enumerate(self.details):
            if d.name == detail.name:
                self.details[i] = new_detail

    def repair(self, detail: Detail):
        for i, d in enumerate(self.details):
            if d.name == detail.name:
                self.details[i] = Detail(d.name, d.performance)

    def __str__(self):
        return "\n".join(str(detail) for detail in self.details)