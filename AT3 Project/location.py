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

    def get_exits(self):
        return [neighbor.name for neighbor in self.neighbors]

    def add_object(self, item):
        self.objects.append(item)

    def pick_up(self, item_name):
        for item in self.objects:
            if item.name.lower() == item_name.lower():
                self.objects.remove(item)
                return item
        return None




