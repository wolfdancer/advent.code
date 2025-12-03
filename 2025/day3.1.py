def identify_max_joltage(line):
    """
    Identifies the maximum joltage from a line of digits.

    Rules:
    1. Find the first occurrence of the biggest digit (scan left to right) -> first
    2. If first is the last digit:
       - Find the next biggest digit (scan left to right) -> second
       - Return second * 10 + first
    3. Else:
       - Find the biggest digit from right of first to end -> second
       - Return first * 10 + second
    """
    # Find the maximum digit value
    max_digit = max(line)

    # Find the first occurrence of the biggest digit
    first_index = line.index(max_digit)
    first = int(max_digit)

    # Check if the identified digit is the last digit
    if first_index == len(line) - 1:
        # Scan from left to right and identify the next biggest digit
        remaining_digits = [d for i, d in enumerate(line) if i != first_index]
        second = int(max(remaining_digits))
        return second * 10 + first
    else:
        # Scan from the right of the identified digit to the end
        right_portion = line[first_index + 1:]
        second = int(max(right_portion))
        return first * 10 + second


def main():
    """
    Reads day3.txt, processes each line using identify_max_joltage,
    and prints the sum of all results.
    """
    total = 0

    with open('day3.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                result = identify_max_joltage(line)
                total += result

    print(total)


if __name__ == "__main__":
    main()
