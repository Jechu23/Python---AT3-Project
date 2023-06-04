

class Map:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [['▢' for _ in range(columns)] for _ in range(rows)]
        self.current_row = 0
        self.current_column = 0

    def display_map(self):
        for row in self.grid:
            print(' '.join(row), end='')

    def mark_visited(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.grid[row][column] = 'X'

    def get_current_indices(self):
        return self.current_row, self.current_column

    def set_current_indices(self, row, column):
        self.current_row = row
        self.current_column = column

