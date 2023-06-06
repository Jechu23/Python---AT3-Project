import unittest
from backpack import BackPack
from item import Item

class TestBackPack(unittest.TestCase):
    def setUp(self):
        self.backpack = BackPack()
        self.item1 = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")
        self.item2 = Item("Phone", "A mobile device", "Property1 Value", "Property2 Value")
        self.item3 = Item("Watch", "A timekeeping device", "Property1 Value", "Property2 Value")

    def test_in_backpack(self):
        self.backpack.add(self.item1)
        self.backpack.add(self.item2)
        self.backpack.add(self.item3)

        # Test for existing items
        self.assertEqual(self.backpack.in_backpack(self.item1), 0)  # Laptop should be at index 0
        self.assertEqual(self.backpack.in_backpack(self.item2), 1)  # Phone should be at index 1
        self.assertEqual(self.backpack.in_backpack(self.item3), 2)  # Watch should be at index 2

        # Test for non-existing items
        self.assertEqual(self.backpack.in_backpack(Item("Tablet", "A portable device", "Property1 Value", "Property2 Value")), -1)  # Tablet is not in the backpack
        self.assertEqual(self.backpack.in_backpack(Item("Headphones", "Audio devices", "Property1 Value", "Property2 Value")), -1)  # Headphones are not in the backpack

if __name__ == '__main__':
    unittest.main()

