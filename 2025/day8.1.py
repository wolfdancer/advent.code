from year2025.day8 import read_positions_and_create_pairs


def main():
    # Read positions and create circuits and pairs
    circuits, pairs = read_positions_and_create_pairs('day8.txt')

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
