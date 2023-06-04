class Item:
    def __init__(self, name, description,  property1, property2):
        self.name = name
        self.description = description

        self.property1 = property1
        self.property2 = property2

    def __str__(self):
        return f"{self.name}: {self.description}\nProperty 1: {self.property1}\nProperty 2: {self.property2}"

    def __lt__(self, other):
        return self.name < other.name