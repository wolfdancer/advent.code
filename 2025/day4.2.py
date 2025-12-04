"""
Day 4 Part 2: Iteratively remove @ symbols with fewer than 4 @ neighbors
"""

def update_neighbors(rolls, row, column, value):
    """Increment all neighbor cells by the given value"""
    row_count = len(rolls)
    column_count = len(rolls[0])

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # Skip the center cell itself
            if dr == 0 and dc == 0:
                continue

            neighbor_row = row + dr
            neighbor_column = column + dc

            # Check bounds
            if 0 <= neighbor_row < row_count and 0 <= neighbor_column < column_count:
                rolls[neighbor_row][neighbor_column] += value

def remove_rolls(grid, rolls):
    """Remove cells with '@' and rolls < 4, return count removed"""
    count = 0
    row_count = len(grid)
    column_count = len(grid[0])

    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == '@' and rolls[row][column] < 4:
                update_neighbors(rolls, row, column, -1)
                grid[row][column] = '.'
                count += 1

    return count

def solve(filename):
    # Read the file and determine dimensions
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')

    row_count = len(lines)
    column_count = len(lines[0])

    # Read content into grid
    grid = []
    for line in lines:
        grid.append(list(line))

    # Create rolls array initialized to 0
    rolls = [[0 for _ in range(column_count)] for _ in range(row_count)]

    # Iterate through grid and increment neighbor cells when we find '@'
    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == '@':
                update_neighbors(rolls, row, column, 1)

    # Keep removing rolls while there are rolls to remove
    count = 0
    removed = remove_rolls(grid, rolls)
    while removed != 0:
        count += removed
        removed = remove_rolls(grid, rolls)

    print(count)

if __name__ == '__main__':
    solve('day4.txt')
