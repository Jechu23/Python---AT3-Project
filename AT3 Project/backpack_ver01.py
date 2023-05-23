from backpack import BackPack
import codecs


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


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

            command = input("Enter a command (move, quit): ").lower()

            if command == "quit":
                print("Goodbye!")
                break
            elif command == "move":
                self.move()

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
        else:
            print("Invalid move. Please try again.")

    def print_map(self):
        with open("map.txt", "r", encoding="utf-8") as map_file:
            print(map_file.read())

    def update_map(self):
        with codecs.open("map.txt", "r+", encoding="utf-8") as map_file:
            map_data = map_file.read()
            map_data = map_data.replace("▢", "X", 1)  # Replace the first unvisited location with "X"
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


# Create an instance of the game
game = Game()
print(game.print_map())

# Create locations
game.create_location("Living Room", "You are in a living room.")
game.create_location("Kitchen", "You are in a kitchen.")
game.create_location("Bedroom", "You are in a bedroom.")
game.create_location("Bathroom", "You are in a bathroom")
game.create_location("Gaming room", "You are in Gaming room ")
game.create_location("Garage", "You are in the garage")

# Connect locations
game.connect_locations(game.locations["Living Room"], game.locations["Kitchen"])
game.connect_locations(game.locations["Living Room"], game.locations["Bedroom"])
game.connect_locations(game.locations['Bedroom'], game.locations['Bathroom'])
game.connect_locations(game.locations["Living Room"], game.locations["Gaming room"])
game.connect_locations(game.locations["Living Room"], game.locations["Garage"])

# Create the map file if it doesn't exist
create_map_file()

# Start the game
game.start_game()

# print map
print('The map\n')
game.print_map()
