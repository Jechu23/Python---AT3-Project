from backpack import BackPack
from location import Location
import codecs


# class Location:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.neighbors = []
#         self.objects = []  # Stores the objects present in the location
#
#     def add_neighbor(self, neighbor):
#         self.neighbors.append(neighbor)
#
#     def get_objects(self):
#         return self.objects


class Game:
    def __init__(self):
        self.locations = {}
        self.current_location = None
        self.backpack = BackPack([])

    def create_location(self, name, description):
        location = Location(name, description)
        self.locations[name] = location

    def connect_locations(self, loc1, loc2):
        loc1.add_neighbor(loc2)
        loc2.add_neighbor(loc1)

    def start_game(self):
        print("Welcome to the Adventure Game!")
        self.current_location = list(self.locations.values())[0]
        self.play()

    def play(self):
        while True:
            print(self.current_location.name)
            print(self.current_location.description)
            print("Neighbors:", [neighbor.name for neighbor in self.current_location.neighbors])

            command = input("Enter a command (move, look, pick up, quit): ").lower()

            if command == "quit":
                print("Goodbye!")
                break
            elif command == "move":
                self.move()
            elif command == "look":
                self.look()
            elif command == "pick up":
                item = input("Enter the name of the item to pick up: ")
                self.pick_up(item)

    def look(self):
        current_objects = self.current_location.get_objects()
        if current_objects:
            print("You see the following objects in the", self.current_location.name + ":")
            for obj in current_objects:
                print(obj)
        else:
            print("There are no objects in the", self.current_location.name + ".")

    def pick_up(self, item):
        current_objects = self.current_location.get_objects()
        if item in current_objects:
            self.backpack.add(item)
            current_objects.remove(item)
            print("You picked up the", item + ".")
        else:
            print("The", item, "is not available in the", self.current_location.name + ".")

    def move(self):
        # Create a dictionary to store valid moves
        valid_moves = {}

        # Iterate over the neighboring locations of the current location
        for i, neighbor in enumerate(self.current_location.neighbors):
            # If the neighbor is already in valid_moves, append the move number to the key
            if neighbor in valid_moves:
                valid_moves[str(valid_moves[neighbor]) + ', ' + str(i + 1)] = neighbor
            else:
                # Otherwise, add the neighbor as a valid move with the move number as the key
                valid_moves[str(i + 1)] = neighbor

        # Display the available moves to the player
        print("Available moves:", list(valid_moves.keys()))

        # Prompt the player to enter the number of the location to move
        move = input("Enter the number of the location to move: ")

        # Check if the entered move is a valid move
        if move in valid_moves:
            # Update the current location based on the selected move
            self.current_location = valid_moves[move]
            self.update_map()  # Update the map file after moving
            self.print_map()
        else:
            print("Invalid move. Please try again.")

    def print_map(self):
        with open("map.txt", "r", encoding="utf-8") as map_file:
            print(map_file.read())

    def update_map(self):
        with codecs.open("map.txt", "r+", encoding="utf-8") as map_file:
            map_data = map_file.read()
            # file = open(location, rb+)
            map_data = map_data.replace("▢", "X", 1)  # Replace the first unvisited location with "X"
            # [x, y] location = x + row_length * y
            # write(b'X')
            map_file.seek(0)
            map_file.write(map_data)


def create_map_file():
    with open("map.txt", "w", encoding="utf-8") as map_file:
        # Initialize the map with unvisited locations represented by "▢"
        map_data = "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n"
        map_file.write(map_data)


if __name__ == '__main__':

    # Create an instance of the game
    game = Game()

    # Create locations
    game.create_location("Living Room", "You are in a cozy living room.")
    game.locations["Living Room"].objects.append("Lamp")
    game.locations["Living Room"].objects.append("TV")

    game.create_location("Kitchen", "You are in a modern kitchen.")
    game.locations["Kitchen"].objects.append("Break")
    game.locations["Kitchen"].objects.append("Apple")

    game.create_location("Bedroom", "You are in a comfortable bedroom.")
    game.locations["Bedroom"].objects.append("Bed")
    game.locations["Bedroom"].objects.append("Dresser")

    game.create_location("Bathroom", "You are in a clean bathroom.")
    game.locations["Bathroom"].objects.append("Toilet")
    game.locations["Bathroom"].objects.append("Towel")

    # Connect locations
    game.connect_locations(game.locations["Living Room"], game.locations["Kitchen"])
    game.connect_locations(game.locations["Living Room"], game.locations["Bedroom"])
    game.connect_locations(game.locations['Bedroom'], game.locations['Bathroom'])



    # Create the map file if it doesn't exist
    create_map_file()

    # Start the game
    game.start_game()

    # print map
    print('The map\n')
    game.print_map()
