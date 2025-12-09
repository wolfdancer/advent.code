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


def main():
    # Initialize circuits map and pairs list
    circuits = {}
    pairs = []

    # Read the file line by line
    with open('day8.txt', 'r') as f:
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

    # Iterate through the first 1000 items in sorted pairs
    for pair in pairs[:1000]:
        # Retrieve the two Sets from circuits
        set_from = circuits[pair.from_pos]
        set_to = circuits[pair.to_pos]

        # Merge the two Sets
        merged_set = set_from | set_to

        # Iterate through items in merged set and update circuits
        for item in merged_set:
            circuits[item] = merged_set

    # Calculate the size of the three largest Sets in circuits values
    unique_sets = {}
    for pos, s in circuits.items():
        set_id = id(s)
        unique_sets[set_id] = s

    # Get sizes of unique sets and sort
    sizes = sorted([len(s) for s in unique_sets.values()], reverse=True)

    # Calculate product of three largest
    result = sizes[0] * sizes[1] * sizes[2]
    print(result)


if __name__ == '__main__':
    main()
