from genus import Genus

class Species(Genus):
    def __init__(self, name, obitanie, vid, characteristics):
        super().__init__(name, obitanie, vid)
        self.characteristics = characteristics

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Характеристика: {self.characteristics}"
