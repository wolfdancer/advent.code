class Position:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, that: 'Position') -> int:
        return (self.x - that.x) ** 2 + (self.y - that.y) ** 2 + (self.z - that.z) ** 2

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Pair:
    def __init__(self, from_pos: Position, to_pos: Position):
        self.from_pos = from_pos
        self.to_pos = to_pos
        self.distance = from_pos.distance(to_pos)


def read_positions_and_create_pairs(filename: str) -> tuple[dict, list]:
    """
    Read positions from file and create circuits and pairs.

    Args:
        filename: Path to the input file containing positions (x,y,z format)

    Returns:
        tuple: (circuits dict, sorted pairs list)
            - circuits: dict mapping Position -> Set of Positions
            - pairs: list of Pair objects sorted by distance
    """
    circuits = {}
    pairs = []

    # Read the file line by line
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Create a position from the line
            x, y, z = map(int, line.split(','))
            position = Position(x, y, z)

            # Iterate through existing items in circuits
            for key, value_set in circuits.items():
                # Get the first item in the Set to create Pair instance
                first_item = next(iter(value_set))
                pair = Pair(first_item, position)
                pairs.append(pair)

            # Create a Set with position as the only item and put it in circuits
            circuits[position] = {position}

    # Sort pairs by distance, lower value first
    pairs.sort(key=lambda p: p.distance)

    return circuits, pairs
