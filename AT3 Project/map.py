

class Map:
    """Class representing the map in the game."""

    def __init__(self, rows, columns):
        """
        Initialize a new map instance.

        Args:
            rows (int): The number of rows in the map.
            columns (int): The number of columns in the map.
        """
        self.rows = rows
        self.columns = columns
        self.grid = [['▢' for _ in range(columns)] for _ in range(rows)]
        self.current_row = 0
        self.current_column = 0

    def display_map(self):
        """
        Display the map grid.

        Prints the grid representation of the map to the console.
        """
        for row in self.grid:
            print(' '.join(row))

    def mark_visited(self, row, column):
        """
        Mark a specific location as visited on the map.

        Args:
            row (int): The row index of the location.
            column (int): The column index of the location.
        """
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.grid[row][column] = 'X'

    def get_current_indices(self):
        """
        Get the current row and column indices.

        Returns:
            tuple: A tuple containing the current row and column indices.
        """
        return self.current_row, self.current_column

    def set_current_indices(self, row, column):
        """
        Set the current row and column indices.

        Args:
            row (int): The new row index.
            column (int): The new column index.
        """
        self.current_row = row
        self.current_column = column

