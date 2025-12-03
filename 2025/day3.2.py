def identify_max_joltage(line, digits):
    """
    Identifies the maximum joltage from a line of digits.

    Rules:
    1. Find the first occurrence of the biggest digit (scan left to right) -> first
    2. If first is at position len(line)-digits+1 or later:
       - Calculate lower_digits from first_index to end
       - Recursively calculate higher_digits from digits before first_index
       - Return concatenation of higher_digits and lower_digits
    3. Else:
       - higher_digit is the digit at first_index
       - Recursively calculate lower_digits from digits after first_index
       - Return concatenation of higher_digit and lower_digits
    """
    # Base case: if we only need 1 digit, return the max digit
    if digits == 1:
        return max(line)

    # Base case: if we have exactly the number of digits we need, return all of them
    if len(line) == digits:
        return line

    # Find the maximum digit value
    max_digit = max(line)

    # Find the first occurrence of the biggest digit
    first_index = line.index(max_digit)

    # Check if the identified digit is at the last (digits-1)th position
    if first_index >= len(line) - digits + 1:
        # Calculate lower_digits from first_index to end
        lower_digits = line[first_index:]

        # Calculate higher_digits through recursive call
        num_lower_digits = len(lower_digits)
        higher_digits = identify_max_joltage(line[:first_index], digits - num_lower_digits)

        # Concatenate and return
        return higher_digits + lower_digits
    else:
        # higher_digit is the digit at first_index
        higher_digit = line[first_index]

        # Calculate lower_digits through recursive call
        lower_digits = identify_max_joltage(line[first_index + 1:], digits - 1)

        # Concatenate and return
        return higher_digit + lower_digits


def main():
    """
    Reads day3.txt, processes each line using identify_max_joltage,
    and prints the sum of all results.
    """
    total = 0

    with open('day3.txt', 'r') as file:
        for line in file:
            result = identify_max_joltage(line.strip(), 12)
            total += int(result)

    print(total)


if __name__ == "__main__":
    main()
