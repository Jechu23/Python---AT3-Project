import unittest
from map import Map

class MapTests(unittest.TestCase):
    def setUp(self):
        self.map = Map(3, 3)

    def test_display_map(self):
        expected_output = "▢ ▢ ▢\n▢ ▢ ▢\n▢ ▢ ▢\n"
        self.assertEqual(self.map.display_map(), expected_output)

    def test_mark_visited(self):
        # Mark a valid location as visited
        self.map.mark_visited(1, 1)
        expected_output = "▢ ▢ ▢\n▢ X ▢\n▢ ▢ ▢\n"
        self.assertEqual(self.map.display_map(), expected_output)

        # Mark an invalid location as visited (outside the map boundaries)
        self.map.mark_visited(4, 4)
        self.assertEqual(self.map.display_map(), expected_output)

    def test_get_current_indices(self):
        self.assertEqual(self.map.get_current_indices(), (0, 0))

    def test_set_current_indices(self):
        self.map.set_current_indices(2, 1)
        self.assertEqual(self.map.get_current_indices(), (2, 1))

if __name__ == '__main__':
    unittest.main()
