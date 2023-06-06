import unittest
import sys
import io
from backpack import BackPack
from item import Item
class TestBackPack(unittest.TestCase):
    def setUp(self):
        self.backpack = BackPack()

    def test_add_item(self):
        item = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        result = backpack.add(item)

        assert result is True
        assert item in backpack.items
        assert backpack.count() == 1

    def test_remove_item(self):
        item = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        backpack.add(item)
        backpack.remove(item)

        assert item not in backpack.items
        assert backpack.count() == 0

    def test_list_items(self):
        item1 = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        backpack.add(item1)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        backpack.list()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        assert item1.name in output

    def test_count_items(self):
        item1 = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        backpack.add(item1)

        assert backpack.count() == 1

    def test_sort_items(self):
        item1 = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")
        item2 = Item("Phone", "A mobile device", "Property1 Value", "Property2 Value")
        item3 = Item("Watch", "A timekeeping device", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        backpack.add(item1)
        backpack.add(item2)
        backpack.add(item3)

        sorted_items = sorted([item1, item2, item3])
        backpack.sort()

        assert backpack.items == sorted_items

    def test_count_specific_item(self):
        item1 = Item("Laptop", "A portable computer", "Property1 Value", "Property2 Value")
        item2 = Item("Phone", "A mobile device", "Property1 Value", "Property2 Value")
        item3 = Item("Watch", "A timekeeping device", "Property1 Value", "Property2 Value")

        backpack = BackPack()
        backpack.add(item1)
        backpack.add(item2)
        backpack.add(item3)

        assert backpack.count_item(item1) == 1
        assert backpack.count_item(item2) == 1
        assert backpack.count_item(item3) == 1


if __name__ == '__main__':
    unittest.main()
