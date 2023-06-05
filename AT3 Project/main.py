from game import Game
from item import Item
from character import Character
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
    game.locations["Living Room"].add_object(
        Item("Lamp", "A bright lamp for illumination", "Beautifully designed", "Provides warm lighting"))
    game.locations["Living Room"].add_object(
        Item("Book", "An interesting book to read", "Classic novel", "Has a bookmark"))

    game.create_location("Kitchen", "You are in a modern kitchen.")
    game.locations["Kitchen"].add_object(
        Item("Key", "A small key for unlocking doors", "Golden key", "Opens secret doors"))
    game.locations["Kitchen"].add_object(
        Item("Apple", "A green delicious fruit", "Organic apple", "Tastes sweet and juicy"))
    game.locations["Kitchen"].add_object(
        Item("Water", "A bottle of sparkling water", "Mineral water", "Keeps you hydrated"))

    game.create_location("Bedroom", "You are in a comfortable bedroom.")
    game.locations["Bedroom"].add_object(
        Item("Phone", "A smartphone for communication", "Smartphone model XYZ", "Has a high-resolution screen"))
    game.locations["Bedroom"].add_object(
        Item("Scarf", "A warm scarf for cold weather", "Knitted scarf", "Soft and cozy"))
    game.locations["Bedroom"].add_object(
        Item("Pillow", "A soft pillow for a good sleep", "Orthopedic pillow", "Provides neck support"))

    game.create_location("Bathroom", "You are in a clean bathroom.")
    game.locations["Bathroom"].add_object(
        Item("Wallet", "A wallet to keep money and cards", "Leather wallet", "Multiple compartments"))
    game.locations["Bathroom"].add_object(
        Item("Towel", "A towel for drying off", "Cotton towel", "Absorbs water quickly"))

    game.create_location("Library", "You are in a quiet library.")
    game.locations["Library"].add_object(
        Item("Book", "A bookshelf full of interesting books", "Reference books", "Contains valuable information"))
    game.locations["Library"].add_object(
        Item("Pencil", "A pencil for writing and drawing", "Mechanical pencil", "Does not require sharpening"))
    game.locations["Library"].add_object(
        Item("Laptop", "A laptop for browsing the internet", "High-performance laptop", "Fast processing speed"))

    game.create_location("Office", "You are in a professional office.")
    game.locations["Office"].add_object(
        Item("GPS", "A GPS device for navigation", "Portable GPS", "Provides accurate directions"))
    game.locations["Office"].add_object(
        Item("Notes", "Important notes and documents", "Confidential documents", "Contains sensitive information"))
    game.locations["Office"].add_object(
        Item("Agenda", "An agenda for organizing tasks", "Leather-bound agenda", "Helps plan daily activities"))

    # Create the Reactor Core
    game.create_location("Reactor Core", "You are in the Reactor Core.")
    game.locations["Reactor Core"].add_object(
        Item("Control Panel", "The control panel for the reactor", "Advanced control panel",
             "Controls reactor functions"))

    # Create the character Jen in the Kitchen
    jen = Character("Jen")
    jen.dialogues = {
        "do you have a match": "Not, I don't have a match.",
        "do you have an apple": "Yes, I  have an apple. Pick up",
        "do you have an water": "Yes, I  have an apple. Pick up",
        "do you have an key": "Yes, I  have an apple. Pick up",
        "where is the reactor core": "The Reactor Core is near the Office, 'Neighbors'. Go to this room. Good luck"
    }
    game.locations["Kitchen"].add_character(jen)

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
    print(Fore.RED + "Your mission is to reach the REACTOR CORE.\n" + Fore.RESET)
    print(Fore.BLUE + "INSTRUCTIONS" + Fore.RESET)
    print(
        Fore.BLUE + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print(" You will navigate through various locations, collect items, and solve puzzles to progress.")
    print(
        Fore.BLUE + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print(Fore.RED + "Use the following commands to play the game:" + Fore.RESET)
    print(" ⚽ 'move <direction>' to go to a neighboring location (e.g. 'N: north').")
    print(" ⚽ 'look' to get a description of your current location.")
    print(" ⚽ 'rucksack' inventory to view the items you have collected.")
    print(" ⚽ 'pick up <item>' to pick up an item in your current location (e.g., 'pick up key').")
    print(" ⚽ 'exit' to exit the game at any time.")
    print(Fore.RED + "IMPORTANT" + Fore.RESET, "Jen is a person inside one of the rooms. You can ask her questions,"
                                               "such as 'where is the reactor core?' She will help you find it")
    print("Good luck and have fun!")
    print("==========================================================================================\n")


if __name__ == '__main__':
    # display_instructions()
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
