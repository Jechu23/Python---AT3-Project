import unittest
from game import Game
from item import Item
from location import Location

class GameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game("Adventure Game")
        self.location1 = self.game.create_location("Location 1", "Description 1")
        self.location2 = self.game.create_location("Location 2", "Description 2")

        self.game = Game("==> WELCOME TO ADVENTURE GAME <==")

    def test_create_location(self):
        self.game.create_location("Location 1", "Description 1")
        self.game.create_location("Location 2", "Description 2")

        self.assertEqual(len(self.game.locations), 2)
        self.assertIn("Location 1", self.game.locations)
        self.assertIn("Location 2", self.game.locations)

    def test_connect_locations(self):
        location1 = Location("Living Room", "You are in a wonderful living room.")
        location2 = Location("Kitchen", "You are in a modern kitchen.")
        self.game.connect_locations(location1, location2)
        # Assert the connection between locations
        assert location1.has_neighbor(location2)
        assert location2.has_neighbor(location1)

    def test_add_object_to_location(self):
        location1 = Location("Living Room", "You are in a wonderful living room.")
        item = Item("Item 1", "Description 1", "Property 1", "Property 2")
        location1.add_object(item)
        # Assert the object is added to the location
        assert item in location1.objects



    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()
