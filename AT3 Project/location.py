class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.neighbors = []
        self.objects = []  # Stores the objects present in the location

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_objects(self):
        return self.objects
