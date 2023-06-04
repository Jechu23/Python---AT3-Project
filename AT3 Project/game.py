from backpack import BackPack
from location import Location
from item import Item
from colorama import Fore


class Game:
    def __init__(self, adventure_name):
        self.adventure_name = adventure_name
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
        print(Fore.CYAN + '==> WELCOME TO ADVENTURE GAME <==' + Fore.RESET)

        # Check if the player has the key to enter the house
        has_key = input(Fore.YELLOW + "Welcome home! Do you have the key to enter? (Yes/No): " + Fore.RESET).lower()
        if has_key == "yes":
            # Create an instance of the key item
            key_item = Item("Key", "A small key for unlocking doors", "Property 1", "Property 2")
            self.backpack.add(key_item)  # Add the key to the backpack
            print("You picked up the key.")

            # Prompt the player to open the door
            open_door = input(Fore.YELLOW + "Do you want to open the door? (Yes/No): " + Fore.RESET).lower()
            if open_door == "yes":
                # Move the player to the living room and start the game
                self.current_location = self.locations["Living Room"]
                print("You opened the door and entered the Living Room.")
                self.play()
            else:
                print("You decided not to open the door. Goodbye!")
        else:
            print("You don't have the key to enter. Goodbye!")

    def display_exits(self):
        exits = self.current_location.get_exits()
        print(Fore.YELLOW + "Available exits:" + Fore.RESET, exits )

    def play(self):
        while True:
            print(self.current_location.name)
            print(self.current_location.description)
            print(Fore.YELLOW + "Neighbors:" + Fore.RESET, [neighbor.name for neighbor in self.current_location.neighbors] )

            command = input(Fore.BLUE + "Enter a command " + Fore.RESET
                            + Fore.RED + "(move, look, pick up, rucksack, quit):"
                            + Fore.RESET).lower()

            if command == "quit":
                print("Goodbye!")
                break
            elif command == "move":
                self.move()
            elif command == "look":
                self.look()
            elif command == "pick up":
                item = input(Fore.MAGENTA + "Enter the name of the item to pick up: " + Fore.RESET)
                self.pick_up_item(item)
            elif command == "rucksack":
                self.display_items()

    def look(self):
        current_objects = self.current_location.get_objects()
        if current_objects:
            print(Fore.LIGHTCYAN_EX + "You see the following objects in the:" + Fore.RESET + Fore.RED, self.current_location.name + ":" + Fore.RESET)
            for obj in current_objects:
                print(obj)
        else:
            print("There are no objects in the", self.current_location.name + ".")

    def pick_up_item(self, item_name):
        item = self.current_location.pick_up(item_name)
        if item is not None:
            if self.backpack.add(item):
                print(f"You picked up {item.name}.")
            else:
                print("Your backpack is full. You can't pick up more items.")
        else:
            print(f"{item_name} is not available in {self.current_location.name}.")

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
        # print("Available moves:", list(valid_moves.keys()))

        # Display the available exits to the player
        self.display_exits()

        # Prompt the player to enter the direction to move
        direction = input(Fore.BLUE + "Enter the direction to move" + Fore.BLUE
                          + Fore.RED + " (N, E, W, S): "
                          + Fore.RESET).upper()

        # Check if the entered direction is a valid move
        valid_moves = {"N": 0, "E": 1, "W": 2, "S": 3}

        if direction in valid_moves:
            move_index = valid_moves[direction]
            if move_index < len(self.current_location.neighbors):
                # Update the current location based on the selected direction
                self.current_location = self.current_location.neighbors[move_index]
                print(Fore.YELLOW + "Moved to:" + Fore.RESET, self.current_location.name )
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid direction. Please try again.")

    def print_map(self):
        with open("map.txt", "r", encoding="utf-8") as map_file:
            map_data = map_file.read()
            print(map_data)

    def display_items(self):
        self.backpack.display_items()


