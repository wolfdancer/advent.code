def can_merge(range1, range2):
    """
    Check if two ranges overlap or are adjacent.
    Returns True if they can be merged, False otherwise.
    """
    # Ranges overlap if one starts before the other ends
    # Also merge if they're adjacent (e.g., range(3,6) and range(6,8))
    return not (range1.stop < range2.start or range2.stop < range1.start)


def merge(range1, range2):
    """
    Merge two ranges into a single range.
    Raises an error if the ranges cannot be merged.
    Returns a new range with the smaller start and larger stop.
    """
    if not can_merge(range1, range2):
        raise ValueError(f"Cannot merge ranges {range1} and {range2} - they don't overlap")

    # Take the smaller start and the larger stop
    new_start = min(range1.start, range2.start)
    new_stop = max(range1.stop, range2.stop)
    return range(new_start, new_stop)


def parse_input(filename):
    """
    Parse the first part of the input file (before the empty line).
    Convert range strings like "3-5" to Python range objects.
    """
    ranges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            # Stop at empty line
            if not line:
                break

            # Parse the range string (format: "start-end")
            parts = line.split('-')
            if len(parts) == 2:
                start = int(parts[0])
                end = int(parts[1])
                # Convert to Python range (end is inclusive, so add 1 to stop)
                ranges.append(range(start, end + 1))

    return ranges


def main():
    # Parse the input file
    ranges = parse_input('day5.txt')

    # Sort by the start of each range
    raw_ranges = sorted(ranges, key=lambda r: r.start)

    # Create merged_ranges list with the first element
    merged_ranges = [raw_ranges[0]]

    # Iterate through remaining ranges
    for current_range in raw_ranges[1:]:
        last_range = merged_ranges[-1]

        if can_merge(current_range, last_range):
            # Merge and replace the last element
            merged_ranges[-1] = merge(current_range, last_range)
        else:
            # Add as a new range
            merged_ranges.append(current_range)

    # Calculate the total size of all merged ranges
    total_size = sum(len(r) for r in merged_ranges)

    print(total_size)


if __name__ == '__main__':
    main()
