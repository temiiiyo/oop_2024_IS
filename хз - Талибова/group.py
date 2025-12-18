
class Group:
    FILE_NAME = "groups.txt"

    def __init__(self, name):
        self.name = name

    def save_to_file(self):
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{self.name}\n")


    def load_all(self):
        with open(Group.FILE_NAME, "r") as file:
            return [line.strip() for line in file]

    def describe(self):
        print(f"Группа: {self.name}")