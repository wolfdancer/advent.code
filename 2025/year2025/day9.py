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


def check_valid_tiles(valid_tiles, rectangle):
    """
    Check if a rectangle is valid based on the valid_tiles map.

    Args:
        valid_tiles: dict mapping row -> range of valid columns
        rectangle: Rectangle object to check

    Returns:
        bool: True if the rectangle is valid, False otherwise
    """
    # Get the column range from the rectangle
    min_col = min(rectangle.pos1.column, rectangle.pos2.column)
    max_col = max(rectangle.pos1.column, rectangle.pos2.column)
    column_range = range(min_col, max_col + 1)

    # Get the row range from the rectangle
    min_row = min(rectangle.pos1.row, rectangle.pos2.row)
    max_row = max(rectangle.pos1.row, rectangle.pos2.row)

    # Check each row in the rectangle
    for row in range(min_row, max_row + 1):
        if row not in valid_tiles:
            return False

        row_column_range = valid_tiles[row]
        # Check if column_range is within row_column_range
        if column_range.start < row_column_range.start or column_range.stop > row_column_range.stop:
            return False

    return True


def parse_sorted_positions(filename):
    """Parse the input file and return a list of Position objects sorted by row."""
    positions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                column, row = map(int, line.split(','))
                positions.append(Position(row, column))
    return sorted(positions, key=lambda p: p.row)
