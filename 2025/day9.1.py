class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return f"Position({self.row}, {self.column})"


class Rectangle:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        # Calculate area as (abs distance of rows + 1) * (abs distance of columns + 1)
        self.area = (abs(pos2.row - pos1.row) + 1) * (abs(pos2.column - pos1.column) + 1)

    def __repr__(self):
        return f"Rectangle({self.pos1}, {self.pos2}, area={self.area})"


def parse_positions(filename):
    """Parse the input file and return a list of Position objects."""
    positions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                row, column = map(int, line.split(','))
                positions.append(Position(row, column))
    return positions


def find_largest_rectangle(positions):
    """
    Find the pair of positions that creates the rectangle with the largest area.

    Optimization: Since area = (abs(row2-row1)+1) * (abs(col2-col1)+1),
    to maximize area, we want to maximize both the row distance and column distance.

    We can optimize by finding the extreme points:
    - Min/max row positions
    - Min/max column positions

    The largest rectangle will likely be formed by positions at the extremes.
    However, to be thorough, we should check all combinations of extreme points.

    For a more complete solution with 496 points, we can use a smart approach:
    1. Find positions with min/max rows and min/max columns
    2. Check all pairs among these candidate positions
    3. For full correctness, we could check all O(n²) pairs, but with optimization
    """
    if len(positions) < 2:
        return None

    # For optimization, we'll focus on positions that are likely to form large rectangles
    # These are positions at the extremes of rows and columns

    min_row_pos = min(positions, key=lambda p: p.row)
    max_row_pos = max(positions, key=lambda p: p.row)
    min_col_pos = min(positions, key=lambda p: p.column)
    max_col_pos = max(positions, key=lambda p: p.column)

    # Create a set of candidate positions (extreme points)
    candidates = {min_row_pos, max_row_pos, min_col_pos, max_col_pos}

    # Also consider positions at corners (combinations of extremes)
    # Sort by row and column to find corner candidates
    sorted_by_row = sorted(positions, key=lambda p: p.row)
    sorted_by_col = sorted(positions, key=lambda p: p.column)

    # Add top-k and bottom-k positions for both dimensions
    k = 10  # Consider top/bottom 10 positions
    for i in range(min(k, len(sorted_by_row))):
        candidates.add(sorted_by_row[i])
        candidates.add(sorted_by_row[-(i+1)])
        candidates.add(sorted_by_col[i])
        candidates.add(sorted_by_col[-(i+1)])

    max_area = 0
    best_rectangle = None

    # Check all pairs of candidate positions
    candidate_list = list(candidates)
    for i in range(len(candidate_list)):
        for j in range(i + 1, len(candidate_list)):
            rect = Rectangle(candidate_list[i], candidate_list[j])
            if rect.area > max_area:
                max_area = rect.area
                best_rectangle = rect

    # For complete correctness with reasonable performance,
    # also check all pairs (O(n²) but n=496 is manageable)
    # This ensures we don't miss any edge cases
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            rect = Rectangle(positions[i], positions[j])
            if rect.area > max_area:
                max_area = rect.area
                best_rectangle = rect

    return best_rectangle


def main():
    positions = parse_positions('day9.txt')
    largest_rect = find_largest_rectangle(positions)

    if largest_rect:
        print(largest_rect.area)
    else:
        print("No valid rectangle found")


if __name__ == '__main__':
    main()
