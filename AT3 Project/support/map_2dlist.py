matrix = [
    ['▢', '▢', '▢',  '▢'],
    ['▢', '▢', '▢',  '▢'],
    ['▢', '▢', '▢',  '▢'],
    ['▢', '▢', '▢',  '▢']
]

# Create a matrix to track visited positions
visited = [[' ' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

# Initial position
current_row = 0
current_column = 0

while True:
    # Print the matrix with the current position marked as ' ' and visited positions
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == current_row and j == current_column:
                print('⚽', end=' ')
            elif visited[i][j] == '⚽':
                print('⚽', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()
    print()

    # Mark the current position as visited with 'X'
    visited[current_row][current_column] = '⚽'

    # Get user input for direction
    direction = input("Enter direction (right = r /left = l /up = u /down= d): ")

    # Update the current position based on the direction
    if direction == 'r':
        current_column += 1
    elif direction == 'l':
        current_column -= 1
    elif direction == 'u':
        current_row -= 1
    elif direction == 'd':
        current_row += 1

    # Check if the current position is valid
    if current_row < 0 or current_row >= len(matrix) or current_column < 0 or current_column >= len(matrix[0]):
        print("Invalid position! Exiting...")
        break
