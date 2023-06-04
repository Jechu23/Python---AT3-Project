from game import Game
from item import Item
from colorama import Fore, Style

def create_map_file():
    with open("map.txt", "w", encoding="utf-8") as map_file:
        # Initialize the map with unvisited locations represented by "▢"
        map_data = "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n" \
                   "▢ ▢ ▢ ▢ ▢\n"
        map_file.write(map_data)


if __name__ == '__main__':
    adventure_name = "==> WELCOME TO ADVENTURE GAME <=="
    # Create an instance of the game
    game = Game(adventure_name)

    # lamp = Item("Lamp", "A bright lamp for illumination", "Property 1 value", "Property 2 value")
    # book = Item("Book", "An interesting book to read", "Property 1 value", "Property 2 value")
    # Create more instances of items with different values for properties

    # Create locations
    game.create_location("Living Room", "You are in a wonderful living room.")
    game.locations["Living Room"].add_object(Item("Lamp", "A bright lamp for illumination", "Property 1", "Property 2"))
    game.locations["Living Room"].add_object(Item("Book", "An interesting book to read", "Property 1", "Property 2"))

    game.create_location("Kitchen", "You are in a modern kitchen.")
    game.locations["Kitchen"].add_object(Item("Key", "A small key for unlocking doors", "Property 1", "Property 2"))
    game.locations["Kitchen"].add_object(Item("Apple", "A green delicious fruit", "Property 1", "Property 2"))
    game.locations["Kitchen"].add_object(Item("Water", "A bottle of sparkling water", "Property 1", "Property 2"))

    game.create_location("Bedroom", "You are in a comfortable bedroom.")
    game.locations["Bedroom"].add_object(Item("Phone", "A smartphone for communication", "Property 1", "Property 2"))
    game.locations["Bedroom"].add_object(Item("scarf", "A smartphone for communication", "Property 1", "Property 2"))
    game.locations["Bedroom"].add_object(Item("Pillow", "A smartphone for communication", "Property 1", "Property 2"))

    game.create_location("Bathroom", "You are in a clean bathroom.")
    game.locations["Bathroom"].add_object(Item("Wallet", "A wallet to keep money and cards", "Property 1", "Property 2"))
    game.locations["Bathroom"].add_object(Item("Towel", "A wallet to keep money and cards", "Property 1", "Property 2"))


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
