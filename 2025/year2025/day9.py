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


def parse_sorted_positions(filename):
    """Parse the input file and return a list of Position objects sorted by row."""
    positions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                row, column = map(int, line.split(','))
                positions.append(Position(row, column))
    return sorted(positions, key=lambda p: p.row)
