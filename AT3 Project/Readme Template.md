# Game Name
- Jesus Huanambal Alejandria
- Id: 20096888

This is a single-player, adventure text-based game.

# Introduction
This game is an exciting adventure where players explore a mysterious world, solve puzzles, interact with characters, and uncover hidden secrets. Get ready for an immersive text-based experience filled with suspense and excitement!

## User Documentation
### Overview and Rules
The game is set in a sprawling mansion filled with intricate rooms, each containing valuable items and clues. The player's goal is to navigate through the mansion, solve puzzles, and ultimately find the hidden treasure.

- Explore various locations within the mansion, each with its unique description and objects.
- Interact with characters to gather information, receive quests, and uncover the secrets of the mansion.
- Use simple commands like "look," "rucksack" or "talk to Jen" to interact with the game world.
- Collect items, solve puzzles, and overcome challenges to progress further in the game.

### Gameplay
- Upon starting the game, players will be introduced to the mansion and its surroundings.
- Players can navigate between different locations by using the available exits.
- Objects in each location can be examined, picked up, or interacted with using appropriate commands.
- Characters within the game can be interacted with by using conversation-based commands, such as asking for information or giving items.
- Players can check their inventory by using the "rucksack" command.
- The objective is to find the hidden treasure within the mansion and successfully complete the game.

## Developer Documentation
### Files and Resources
- `backpack.py`: Contains the implementation of the BackPack class.
- `game.py`: Contains the main game logic and functions.
- `location.py`: Defines the Location class and related methods for managing locations and objects.
- `character.py`: Defines the Character class and related methods for interacting with characters in the game.
- `item.py`: Defines the Item class for creating and managing game items.
- `map.py`: Defines the Map class for displaying the game map and tracking the player's position.
- `test`: Directory test by Unit Test.

### User Requirements Specification
The game should provide the following features:
- A user-friendly interface with clear instructions and prompts.
- Interactive gameplay with the ability to navigate between locations, interact with objects and characters, and solve puzzles.
- A system for managing the player's inventory and displaying the collected items.
- Engaging dialogues and interactions with characters to provide an immersive experience.
- Clear win condition and feedback when the player successfully completes the game.

### Class Diagram - Adventure Game
```mermaid
classDiagram
    Game --* Location
    Game --* Map
    Game --* BackPack
    Game --* Character
    Location --* Item

    class Game {
        - adventure_name
        - locations
        - winning_condition
        + create_location(name, description)
        + connect_locations(location1, location2)
        + start_game()
    }

    class Location {
        - name
        - description
        - neighbors
        - objects
        + add_neighbor(neighbor)
        + has_neighbor(location)
        + get_objects()
        + get_exits()
        + add_object(item)
        + pick_up(item_name)
    }

    class Map {
        - rows
        - columns
        - grid
        - current_row
        - current_column
        + display_map()
        + mark_visited(row, column)
        + get_current_indices()
        + set_current_indices(row, column)
    }

    class BackPack {
        - _backpack
        + __init__(items)
        + items
        + sort()
        + count()
        + list()
        + add(item)
        + remove(item)
        + display_items()
        + in_backpack(item)
        + count_item(item)
    }

    class Character {
        - name
        - dialogue
        + __init__(name, dialogue)
        + get_name()
        + talk()
        + give_item(item)
        + take_item(item)
    }

    class Item {
        - name
        - description
        + __init__(name, description)
        + __str__()
        + __lt__(other)
    }
