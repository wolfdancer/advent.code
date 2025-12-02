def identify_invalid_ids(range_obj):
    """
    Find all numbers within the range where the second half equals the first half.
    Uses an optimized algorithm to jump through candidates instead of checking every number.
    """
    invalid_ids = []
    current = range_obj.start

    while current < range_obj.stop:
        num_str = str(current)
        num_digits = len(num_str)

        # If odd number of digits, jump to next number with even digits
        if num_digits % 2 == 1:
            current = 10 ** num_digits
            continue

        # Even number of digits - split into two halves
        half_len = num_digits // 2
        first_half = num_str[:half_len]
        second_half = num_str[half_len:]

        if first_half > second_half:
            # Replace second half with first half
            candidate = int(first_half + first_half)
        elif first_half == second_half:
            # Found an invalid ID
            invalid_ids.append(current)
            # Next candidate: increment first half by 1
            first_half_int = int(first_half) + 1
            # Check for overflow
            if len(str(first_half_int)) > half_len:
                # Overflow - jump to next power of 10
                candidate = 10 ** num_digits
            else:
                # No overflow - use incremented first half
                first_half_str = str(first_half_int).zfill(half_len)
                candidate = int(first_half_str + first_half_str)
        else:  # first_half < second_half
            # Increment first half by 1
            first_half_int = int(first_half) + 1
            # Check for overflow
            if len(str(first_half_int)) > half_len:
                # Overflow - jump to next power of 10
                candidate = 10 ** num_digits
            else:
                # No overflow - use incremented first half
                first_half_str = str(first_half_int).zfill(half_len)
                candidate = int(first_half_str + first_half_str)

        current = candidate

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
