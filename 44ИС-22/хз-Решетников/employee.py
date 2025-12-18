class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.position}"

if __name__ == "__main__":
    pass