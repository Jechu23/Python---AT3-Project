import sys
from backpack import BackPack
from location import Location
from item import Item
from map import Map
from colorama import Fore


class Game:
    def __init__(self, adventure_name):
        """
        Initialize the Game object with the provided adventure name.

        param adventure_name: The name of the adventure game.
        """
        self.adventure_name = adventure_name
        self.locations = {}
        self.current_location = None
        self.backpack = BackPack([])
        self.game_map = Map(3, 3)  # Adjust the size according to your map dimensions
        self.goal = "Re-engage the safety system of the reactor core to prevent a core meltdown."

    def create_location(self, name, description):
        """
        Create a new location with the provided name and description and add it to the game.

        param name: The name of the location.
        param description: The description of the location.
        """
        location = Location(name, description)
        self.locations[name] = location

    def connect_locations(self, loc1, loc2):
        """
        Connect two locations together as neighboring locations.

        param loc1: The first location.
        param loc2: The second location.
        """
        loc1.add_neighbor(loc2)
        loc2.add_neighbor(loc1)

    def start_game(self):
        """
        Start the adventure game.
        """
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
                self.play_again()
        else:
            print("You don't have the key to enter. Goodbye!")
            self.play_again()

    def display_exits(self):
        """
        Display the available exits from the current location.
        """
        exits = self.current_location.get_exits()
        print(Fore.YELLOW + "Available exits:" + Fore.RESET, exits)

    def display_characters(self):
        current_location = self.current_location
        characters = []
        if current_location.characters:
            for character in current_location.characters:
                characters.append(character.name)
        return characters

    def play(self):
        """
        Play the adventure game.
        """
        while True:
            print(self.current_location.name)
            print(self.current_location.description)
            print(Fore.YELLOW + "Neighbors:" + Fore.RESET,
                  [neighbor.name for neighbor in self.current_location.neighbors])
            characters = self.display_characters()
            if characters:
                print(Fore.LIGHTCYAN_EX + "Characters in the current location: " + Fore.RESET)
                for character in characters:
                    print(character + Fore.LIGHTBLUE_EX + ": Write 'talk' to have a conversation with her." + Fore.RESET)
            else:
                print(Fore.GREEN + "No characters in this location." + Fore.RESET)

            command = input(Fore.BLUE + "Enter a command " + Fore.RESET
                            + Fore.RED + "(move, look, pick up, rucksack, exit):"
                            + Fore.RESET).lower()

            if command == "exit":
                print("Goodbye!")
                self.play_again()

            elif command == "move":
                self.move()
            elif command == "look":
                self.look()
            elif command == "pick up":
                item = input(Fore.MAGENTA + "Enter the name of the item to pick up: " + Fore.RESET)
                self.pick_up_item(item)
            elif command == "rucksack":
                self.display_items()
            elif command == "talk":
                self.current_location.talk()

    def look(self):
        """
        Look for objects in the current location and display them.
        """
        current_objects = self.current_location.get_objects()
        if current_objects:
            print(Fore.LIGHTCYAN_EX + "You see the following objects in the:" + Fore.RESET + Fore.RED,
                  self.current_location.name + ":" + Fore.RESET)
            for obj in current_objects:
                print(obj)
        else:
            print("There are no objects in the", self.current_location.name + ".")

    def pick_up_item(self, item_name):
        """
        Pick up an item from the current location and add it to the backpack.

        param item_name: The name of the item to pick up.
        """
        item = self.current_location.pick_up(item_name)
        if item is not None:
            if self.backpack.add(item):
                print(f"You picked up {item.name}.")
            else:
                print("Your backpack is full. You can't pick up more than 5 items.")
        else:
            print(f"{item_name} is not available in {self.current_location.name}.")

    def move(self):
        """
        Move to a neighboring location based on the player's input.
        """
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
                print(Fore.YELLOW + "Moved to:" + Fore.RESET, self.current_location.name)

                # Update the map to mark the new location as visited
                self.game_map.mark_visited(move_index, move_index)

                # Get the current row and column indices
                current_row, current_column = self.game_map.get_current_indices()

                move_row = None
                move_column = None

                # Determine the new row and column indices based on the direction
                if direction == "N":
                    move_row = current_row - 1
                    move_column = current_column
                elif direction == "E":
                    move_row = current_row
                    move_column = current_column + 1
                elif direction == "S":
                    move_row = current_row + 1
                    move_column = current_column
                elif direction == "W":
                    move_row = current_row
                    move_column = current_column - 1

                # Update the current indices in the map
                self.game_map.set_current_indices(move_row, move_column)
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid direction. Please try again.")

        # print("Adventure Map:")
        # self.game_map.display_map()

        if self.current_location.name == "Reactor Core":
            print(Fore.GREEN + "\n CONGRATULATIONS! You successfully re-engaged the safety system of the reactor core.")
            print(Fore.BLUE + "You have prevented a core meltdown. YOU WIN! \n" + Fore.RESET)
            self.play_again()

    def display_items(self):
        self.backpack.display_items()

    def play_again(self):
        while True:
            option = input("Option 1: Exit the game.\n"
                           "Option 2: Start again\n"
                           "Enter your option (1/2): ").strip()
            if option == "1":
                print("Goodbye!")
                # You can use the `sys` module to exit the program
                sys.exit(0)  # Exit the program with a successful status
            elif option == "2":
                self.start_game()
                break
            else:
                print("Invalid option. Please choose 1 or 2.")
