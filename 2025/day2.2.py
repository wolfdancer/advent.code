def increase_leader(leader, num_parts):
    """
    Increase the leader by 1 and return the repeated pattern for num_parts.
    If leader overflows to next power of 10, return 1 followed by zeros.

    Examples:
    - increase_leader(99, 3) -> 1000000 (overflow case)
    - increase_leader(28, 4) -> 29292929 (no overflow)
    """
    leader_str = str(leader)
    leader_len = len(leader_str)
    next_leader = leader + 1
    next_leader_str = str(next_leader)

    # Check if it overflows to next power of 10
    if len(next_leader_str) > leader_len:
        # Return 1 followed by zeros (length = leader_len * num_parts)
        return 10 ** (leader_len * num_parts)
    else:
        # Repeat the new leader num_parts times
        return int(next_leader_str * num_parts)


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
        next_power = 10 ** num_digits

        # Try all possible equal-length partitions (2, 3, 4, ... num_digits)
        for num_parts in range(2, num_digits + 1):
            # Check if digits can be evenly divided
            if num_digits % num_parts != 0:
                continue

            part_len = num_digits // num_parts
            candidate = current

            # Middle candidates-loop: iterate all identified candidates
            while candidate < next_power and candidate < range_obj.stop:
                candidate_str = str(candidate)

                # Extract all parts
                parts = [candidate_str[i*part_len:(i+1)*part_len] for i in range(num_parts)]
                leader = int(parts[0])

                finished = True

                # Inner validating-loop: compare leader to other parts
                for i in range(1, num_parts):
                    checked_part = int(parts[i])

                    if leader > checked_part:
                        # Replace all parts with leader's value
                        candidate = int(parts[0] * num_parts)
                        finished = False
                        break
                    elif leader < checked_part:
                        # Increase leader and set candidate
                        candidate = increase_leader(leader, num_parts)
                        finished = False
                        break

                # If finished without breaking, all parts are equal
                if finished:
                    invalid_ids.add(candidate)
                    candidate = increase_leader(leader, num_parts)

        # Jump to next power of 10
        current = next_power

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
