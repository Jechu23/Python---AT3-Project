from game import Game
from item import Item
from colorama import Fore

adventure_name = "==> WELCOME TO ADVENTURE GAME <=="


def create_game():
    """
    Create an instance of the adventure game and set up the game world.

    :return: The created game object.
    """

    # Create an instance of the game
    game = Game(adventure_name)

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
    game.locations["Bedroom"].add_object(Item("Scarf", "A warm scarf for cold weather", "Property 1", "Property 2"))
    game.locations["Bedroom"].add_object(Item("Pillow", "A soft pillow for a good sleep", "Property 1", "Property 2"))

    game.create_location("Bathroom", "You are in a clean bathroom.")
    game.locations["Bathroom"].add_object(Item("Wallet", "A wallet to keep money and cards", "Property 1", "Property 2"))
    game.locations["Bathroom"].add_object(Item("Towel", "A towel for drying off", "Property 1", "Property 2"))

    game.create_location("Library", "You are in a quiet library.")
    game.locations["Library"].add_object(Item("Book", "A bookshelf full of interesting books", "Property 1", "Property 2"))
    game.locations["Library"].add_object(Item("Pencil", "A pencil for writing and drawing", "Property 1", "Property 2"))
    game.locations["Library"].add_object(Item("Laptop", "A laptop for browsing the internet", "Property 1", "Property 2"))

    game.create_location("Office", "You are in a professional office.")
    game.locations["Office"].add_object(Item("GPS", "A GPS device for navigation", "Property 1", "Property 2"))
    game.locations["Office"].add_object(Item("Notes", "Important notes and documents", "Property 1", "Property 2"))
    game.locations["Office"].add_object(Item("Agenda", "An agenda for organizing tasks", "Property 1", "Property 2"))

    # Create the Reactor Core
    game.create_location("Reactor Core", "You are in the Reactor Core.")
    game.locations["Reactor Core"].add_object(Item("Control Panel", "The control panel for the reactor", "Property 1", "Property 2"))

    # Connect locations
    game.connect_locations(game.locations["Living Room"], game.locations["Kitchen"])
    game.connect_locations(game.locations["Living Room"], game.locations["Bedroom"])
    game.connect_locations(game.locations["Bedroom"], game.locations["Bathroom"])
    game.connect_locations(game.locations["Living Room"], game.locations["Library"])
    game.connect_locations(game.locations["Library"], game.locations["Living Room"])
    game.connect_locations(game.locations["Library"], game.locations["Bathroom"])
    game.connect_locations(game.locations["Bathroom"], game.locations["Living Room"])
    game.connect_locations(game.locations["Living Room"], game.locations["Office"])
    game.connect_locations(game.locations["Office"], game.locations["Library"])
    game.connect_locations(game.locations["Office"], game.locations["Reactor Core"])

    # Set the winning condition
    game.winning_condition = game.locations["Reactor Core"]

    return game


def display_instructions():
    print(Fore.BLUE + "\n========== ADVENTURE GAME INSTRUCTIONS ==========" + Fore.RESET)
    print("Welcome to the Adventure Game!")
    print(Fore.RED+"Your mission is to reach the REACTOR CORE.\n" + Fore.RESET)
    print(Fore.BLUE + "INSTRUCTIONS" + Fore.RESET)
    print(Fore.BLUE + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print(" You will navigate through various locations, collect items, and solve puzzles to progress.")
    print(Fore.BLUE + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print(Fore.RED + "Use the following commands to play the game:" + Fore.RESET)
    print(" ⚽ 'go <direction>' to move to a neighboring location (e.g., 'N north').")
    print(" ⚽ 'look' to get a description of your current location.")
    print(" ⚽ 'rucksack' inventory to view the items you have collected.")
    print(" ⚽ 'pick up <item>' to pick up an item in your current location (e.g., 'pick up key').")
    print(" ⚽ 'quit' to exit the game at any time.")
    print("Good luck and have fun!")
    print("==========================================================================================\n")


if __name__ == '__main__':
    display_instructions()
    main_game = create_game()

    while True:
        print(Fore.LIGHTGREEN_EX + "==== Adventure Game Menu ====")
        print("= Option 1: Exit the game   =")
        print("= Option 2: Start again     =")
        print("=============================" + Fore.RESET)
        option = input(Fore.BLUE + "Enter your option (1/2): " + Fore.RESET)

        if option == "1":
            print("Exiting the game. Goodbye!")
            break
        elif option == "2":
            print("Starting a new game...")
            display_instructions()
            main_game = create_game()
            main_game.start_game()
        else:
            print("Invalid option. Please try again.")
