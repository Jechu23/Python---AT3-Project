

class Location:
    """Class representing a location in the game."""

    def __init__(self, name, description):
        """
        Initialize a new location instance.

        Args:
        name (str): The name of the location.
        description (str): The description of the location.
        """
        self.name = name
        self.description = description
        self.neighbors = []
        self.objects = []  # Stores the objects present in the location

    def add_neighbor(self, neighbor):
        """
        Add a neighboring location to this location.

        Args:
        neighbor (Location): The neighboring location to add.
        """
        self.neighbors.append(neighbor)

    def has_neighbor(self, location):
        """
        Check if this location has a specific neighboring location.

        Args:
        location (Location): The location to check for.

        Returns:
        bool: True if the specified location is a neighbor, False otherwise.
        """
        return location in self.neighbors

    def get_objects(self):
        """
        Get the list of objects present in the location.

        Returns:
        list: The list of objects in the location.
        """
        return self.objects

    def get_exits(self):
        """
        Get the list of exit names for this location.

        Returns:
        list: The list of exit names.
        """
        return [neighbor.name for neighbor in self.neighbors]

    def add_object(self, item):
        """
        Add an object to the location.

        Args:
        item (Item): The item object to add.
        """
        self.objects.append(item)

    def pick_up(self, item_name):
        """
        Remove and return an item from the location based on its name.

        Args:
        item_name (str): The name of the item to pick up.

        Returns:
        Item or None: The item object if found, None otherwise.
        """
        for item in self.objects:
            if item.name.lower() == item_name.lower():
                self.objects.remove(item)
                return item
        return None






