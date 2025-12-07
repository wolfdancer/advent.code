# Memoization cache to avoid recalculating the same (row, column) positions
cache = {}

def calculate_timeline(manifold, row, column):
    """
    Recursively calculate the number of timelines through the manifold.

    Args:
        manifold: 2D array of characters
        row: Current row index
        column: Current column index

    Returns:
        Number of valid paths from this position
    """
    # Check cache first
    if (row, column) in cache:
        return cache[(row, column)]

    # Check if column is out of bounds (left)
    if column < 0:
        return 0

    # Check if column is out of bounds (right)
    if column >= len(manifold[0]):
        return 0

    # Move to next row
    row += 1

    # Check if we've reached the end (past the last row)
    if row == len(manifold):
        return 1

    # If current position is '.', continue straight down
    if manifold[row][column] == '.':
        result = calculate_timeline(manifold, row, column)
    else:
        # Otherwise (hit a '^'), the beam splits into left and right
        # Return sum of both paths
        left_path = calculate_timeline(manifold, row, column - 1)
        right_path = calculate_timeline(manifold, row, column + 1)
        result = left_path + right_path

    # Cache the result before returning
    cache[(row, column)] = result
    return result


# Read the input file into a 2D array
with open('day7.txt', 'r') as f:
    lines = f.readlines()

# Create manifold as 2D array of characters
manifold = []
for line in lines:
    manifold.append(list(line.rstrip('\n')))

# Find the index of 'S' in the first line
first_line = manifold[0]
column = first_line.index('S')

# Calculate and print the result
result = calculate_timeline(manifold, 0, column)
print(result)
