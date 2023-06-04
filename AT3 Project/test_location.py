import unittest
from location import Location
from item import Item

class LocationTests(unittest.TestCase):
    def setUp(self):
        self.location = Location("Living Room", "You are in a wonderful living room.")

    def test_add_neighbor(self):
        neighbor = Location("Kitchen", "You are in a modern kitchen.")
        self.location.add_neighbor(neighbor)
        self.assertIn(neighbor, self.location.neighbors)

    def test_has_neighbor(self):
        neighbor = Location("Kitchen", "You are in a modern kitchen.")
        self.location.add_neighbor(neighbor)
        self.assertTrue(self.location.has_neighbor(neighbor))

    def test_get_objects(self):
        item1 = Item("Item 1", "Description 1", "Property 1", "Property 2")
        item2 = Item("Item 2", "Description 2", "Property 3", "Property 4")
        self.location.add_object(item1)
        self.location.add_object(item2)
        objects = self.location.get_objects()
        self.assertIn(item1, objects)
        self.assertIn(item2, objects)

    def test_get_exits(self):
        neighbor1 = Location("Kitchen", "You are in a modern kitchen.")
        neighbor2 = Location("Bathroom", "You are in a clean bathroom.")
        self.location.add_neighbor(neighbor1)
        self.location.add_neighbor(neighbor2)
        exits = self.location.get_exits()
        self.assertEqual(exits, ["Kitchen", "Bathroom"])

    def test_add_object(self):
        item = Item("Item 1", "Description 1", "Property 1", "Property 2")
        self.location.add_object(item)
        self.assertIn(item, self.location.objects)

    def test_pick_up(self):
        item = Item("Item 1", "Description 1", "Property 1", "Property 2")
        self.location.add_object(item)

        # Test picking up an existing item
        picked_item = self.location.pick_up("Item 1")
        self.assertEqual(picked_item, item)
        self.assertNotIn(item, self.location.objects)

        # Test picking up a non-existing item
        picked_item = self.location.pick_up("Non-existing Item")
        self.assertIsNone(picked_item)

if __name__ == '__main__':
    unittest.main()
