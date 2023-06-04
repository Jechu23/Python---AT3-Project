class Item:
    """Class representing an item in the game."""

    def __init__(self, name, description, property1, property2):
        """
        Initialize a new item instance.

        Args:
            name (str): The name of the item.
            description (str): The description of the item.
            property1 (str): The first property of the item.
            property2 (str): The second property of the item.
        """

        self.name = name
        self.description = description

        self.property1 = property1
        self.property2 = property2

    def __str__(self):
        """
        Return a string representation of the item.

        Returns:
        str: The string representation of the item.
        """
        return f"{self.name}: {self.description}\nProperty 1: {self.property1}\nProperty 2: {self.property2}"

    def __lt__(self, other):
        """
        Compare two items based on their names.

        Args:
        other (Item): The other item to compare.

        Returns:
        bool: True if this item's name is less than the other item's name, False otherwise.
        """
        return self.name < other.name
