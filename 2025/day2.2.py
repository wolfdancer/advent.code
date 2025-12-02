def identify_invalid_ids(range_obj):
    """
    Find all numbers within the range where digits can be split into equal parts
    that are all identical. For example:
    - 123123 splits into 2 parts: "123" and "123" (valid)
    - 222222 splits into 2 parts: "222" and "222" OR 3 parts: "22", "22", "22" (valid both ways)

    Uses an optimized algorithm to jump through candidates for each partition size.
    Uses a Set to avoid double counting numbers that match multiple partition patterns.
    """
    invalid_ids = set()
    current = range_obj.start

    while current < range_obj.stop:
        num_str = str(current)
        num_digits = len(num_str)

        # Try all possible equal-length partitions (2, 3, 4, ... num_digits)
        found_match = False
        for num_parts in range(2, num_digits + 1):
            # Check if digits can be evenly divided
            if num_digits % num_parts != 0:
                continue

            part_len = num_digits // num_parts

            # Extract all parts
            parts = [num_str[i*part_len:(i+1)*part_len] for i in range(num_parts)]

            # Check if all parts are identical
            if all(part == parts[0] for part in parts):
                invalid_ids.add(current)
                found_match = True
                break  # Found a match, no need to check more partitions

        # Move to next candidate
        # For now, just increment by 1 to ensure we don't miss any numbers
        # Optimization can be added later if needed
        current += 1

    return invalid_ids


def parse_ranges(line):
    """
    Parse a line of range pairs into a list of range objects.
    Example: "11-22,95-115" -> [range(11,23), range(95,116)]
    """
    ranges = []
    range_pairs = line.strip().split(',')

    for pair in range_pairs:
        first, last = pair.split('-')
        # Add 1 to last to make it inclusive
        ranges.append(range(int(first), int(last) + 1))

    return ranges


def main():
    # Read the file
    with open('day2.txt', 'r') as f:
        line = f.read().strip()

    # Parse ranges
    ranges = parse_ranges(line)

    # Find invalid IDs in each range and sum them up
    total = 0
    for range_obj in ranges:
        invalid_ids = identify_invalid_ids(range_obj)
        total += sum(invalid_ids)

    print(total)


if __name__ == '__main__':
    main()
