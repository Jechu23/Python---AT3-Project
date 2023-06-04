import unittest
from item import Item

class ItemTests(unittest.TestCase):
    def setUp(self):
        self.item = Item("Key", "A small key for unlocking doors", "Property 1", "Property 2")

    def test_str(self):
        expected_str = "Key: A small key for unlocking doors\nProperty 1: Property 1\nProperty 2: Property 2"
        self.assertEqual(str(self.item), expected_str)

    def test_lt(self):
        item1 = Item("Item 1", "Description 1", "Property 1", "Property 2")
        item2 = Item("Item 2", "Description 2", "Property 3", "Property 4")
        item3 = Item("Item 3", "Description 3", "Property 5", "Property 6")

        # Test item1 < item2
        self.assertLess(item1, item2)

        # Test item2 < item3
        self.assertLess(item2, item3)

        # Test item1 < item3
        self.assertLess(item1, item3)

        # Test item1 < item1 (should return False)
        self.assertFalse(item1 < item1)

if __name__ == '__main__':
    unittest.main()
