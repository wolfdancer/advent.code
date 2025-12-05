def is_fresh(ranges, id):
    """
    Check if the id is within one of the ranges.

    Args:
        ranges: List of range objects
        id: Integer to check

    Returns:
        True if id is in any of the ranges, False otherwise
    """
    for r in ranges:
        if id in r:
            return True
    return False


def parse_input(filename):
    """
    Parse the input file into fresh_ids ranges and ingredient_ids.

    Args:
        filename: Path to input file

    Returns:
        Tuple of (fresh_ids, ingredient_ids)
    """
    with open(filename, 'r') as f:
        content = f.read()

    # Split by empty line
    parts = content.strip().split('\n\n')

    # Parse first part - convert "3-5" to range(3, 6)
    fresh_ids = []
    for line in parts[0].strip().split('\n'):
        start, end = map(int, line.split('-'))
        fresh_ids.append(range(start, end + 1))  # +1 because range is exclusive at end

    # Parse second part - get ingredient IDs
    ingredient_ids = [int(line) for line in parts[1].strip().split('\n')]

    return fresh_ids, ingredient_ids


def main():
    # Read and parse the input file
    fresh_ids, ingredient_ids = parse_input('day5.txt')

    # Count how many ingredients are fresh
    fresh_count = sum(1 for ingredient in ingredient_ids if is_fresh(fresh_ids, ingredient))

    print(fresh_count)


if __name__ == '__main__':
    main()
