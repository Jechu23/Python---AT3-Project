# Map representation
map_grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '.', '.', '.', '.', '.', '.', ' ', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', ' ', '.', '.', '.', '.', '.', '.', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Player position
player_x = 4
player_y = 5

# Game loop
while True:
    # Display the map
    for row in map_grid:
        print(' '.join(row))

    # Get user input
    direction = input("Enter a direction (w/a/s/d): ")

    # Update player position
    if direction == 'w':  # Move up
        if map_grid[player_y - 1][player_x] != '#':
            player_y -= 1
    elif direction == 'a':  # Move left
        if map_grid[player_y][player_x - 1] != '#':
            player_x -= 1
    elif direction == 's':  # Move down
        if map_grid[player_y + 1][player_x] != '#':
            player_y += 1
    elif direction == 'd':  # Move right
        if map_grid[player_y][player_x + 1] != '#':
            player_x += 1

    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
