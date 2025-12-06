#!/usr/bin/env python3
"""
Day 6 Part 2: Parse numbers in columns and process with operators
"""

def parse_and_calculate(filename):
    numbers = []

    with open(filename, 'r') as f:
        for line in f:
            # Check if this is the operator line (starts with '*' or '+')
            stripped = line.lstrip()
            if stripped and (stripped[0] == '*' or stripped[0] == '+'):
                # Process operator line
                result = 0
                current_value = 0
                current_operator = None

                for i, char in enumerate(line):
                    if char == '*' or char == '+':
                        # Add current_value to result
                        result += current_value

                        # Get the matching value from numbers array
                        if i < len(numbers) and numbers[i] is not None:
                            current_value = numbers[i]
                        else:
                            current_value = 0

                        # Set the operator
                        current_operator = char
                    elif i < len(numbers) and numbers[i] is not None:
                        # Perform calculation if we have an operator
                        if current_operator is not None:
                            if current_operator == '+':
                                current_value = current_value + numbers[i]
                            elif current_operator == '*':
                                current_value = current_value * numbers[i]

                # Add the final current_value to result
                result += current_value

                print(result)
                break
            else:
                # Parse number line
                # Check if we need to expand numbers array
                if len(line) > len(numbers):
                    numbers.extend([None] * (len(line) - len(numbers)))

                # Iterate through each character in the line
                for i, char in enumerate(line):
                    # If it's empty (space or newline), continue
                    if char == ' ' or char == '\n' or char == '\t':
                        continue

                    # If it's a digit
                    if char.isdigit():
                        value = int(char)

                        # Check the matching item in numbers
                        if numbers[i] is None:
                            numbers[i] = value
                        else:
                            numbers[i] = numbers[i] * 10 + value

if __name__ == '__main__':
    parse_and_calculate('day6.txt')
