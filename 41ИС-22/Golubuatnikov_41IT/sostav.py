class Sostav:
    def __init__(self, teplovoz):
        self.teplovoz = teplovoz
        self.vagons = []

    def add_vagon(self, vagon):
        self.vagons.append(vagon)

    def info(self):
        vagon_info = [vagon.info() for vagon in self.vagons]
        return f'{self.teplovoz.info()}\nСостав вагонов:\n' + '\n'.join(vagon_info)

    def write_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.info())

