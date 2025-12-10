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

    Optimized solution with early pruning:
    1. Sort positions by row (O(n log n))
    2. Pre-compute global column min/max for pruning (O(n))
    3. For each position, check others with early termination (O(n²) worst case,
       but significantly faster in practice due to pruning)

    Optimization strategies:
    - Early termination when remaining row distance can't beat current max
    - Sorted order allows skipping positions once area can't improve
    - Pre-computed column bounds avoid repeated calculations

    Time complexity: O(n²) worst case, but much faster in practice
    Space complexity: O(n)
    """
    if len(positions) < 2:
        return None

    # Sort positions by row coordinate
    sorted_positions = sorted(positions, key=lambda p: p.row)

    # Pre-compute global column bounds for pruning
    min_col = min(p.column for p in positions)
    max_col = max(p.column for p in positions)
    max_col_dist = max_col - min_col + 1

    max_area = 0
    best_rectangle = None

    # For each position, check all positions after it in sorted order
    for i in range(len(sorted_positions)):
        # Maximum possible row distance from this position
        max_possible_row_dist = sorted_positions[-1].row - sorted_positions[i].row + 1

        # Early termination: if we can't possibly beat the current max area
        # even with the maximum possible column distance, we can stop
        if max_possible_row_dist * max_col_dist <= max_area:
            break

        for j in range(i + 1, len(sorted_positions)):
            rect = Rectangle(sorted_positions[i], sorted_positions[j])
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
