import json


class BackPack:
    """
    BackPack Class

    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items
    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if not isinstance(items, list):
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return len(self._backpack)

    def list(self):
        return self._backpack

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        low = 0
        high = len(self._backpack) - 1

        while low <= high:
            mid = (low + high) // 2
            if self._backpack[mid] == item:
                return mid
            elif self._backpack[mid] < item:
                low = mid + 1
            else:
                high = mid - 1

        return -1

# location >=2
# items > = 2 (character)
# grid >= 9
# Binary search
# Randon Access file
# Ransack
# Use a dictionary not Json File

class Player:
    """
    Player Class

    ToDo: [X] Initialize player with a starting location
    ToDo: [X] Move player to available locations
    ToDo: [X] Display available directions for the current location
    """

    def __init__(self, starting_location):
        self.current_location = self.get_location(starting_location)

    def get_location(self, location_name):
        for location in data["locations"]:
            if location["name"] == location_name:
                return location
        return None

    def move(self, direction):
        available_directions = self.current_location.get("directions", {})
        if direction in available_directions:
            next_location_name = available_directions[direction]
            self.current_location = self.get_location(next_location_name)
            print("Player moved to", self.current_location["name"])
        else:
            print("Invalid direction. Choose from:", ", ".join(available_directions.keys()))

    def display_available_directions(self):
        available_directions = self.current_location.get("directions", {})
        if available_directions:
            print("Available directions:", ", ".join(available_directions.keys()))
        else:
            print("No available directions.")


# Read the location data from the JSON file
with open("location.json", "r") as json_file:
    data = json.load(json_file)

# Create the backpack
backpack_items = ["book", "water bottle", "snacks"]
backpack = BackPack(backpack_items)

# Create the player
player = Player(data["locations"][0]["name"])  # Set the starting location here

# Game loop
while True:
    print("Current location:", player.current_location["name"])
    player.display_available_directions()
    action = input("Enter a direction (N, S, W, E) to move or 'Q' to quit: ").upper()

    if action == "Q":
        print("Game over.")
        break
    elif action in ["N", "S", "W", "E"]:
        player.move(action)
    else:
        print("Invalid action. Please try again.")
