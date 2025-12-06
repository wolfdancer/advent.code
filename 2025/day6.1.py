#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6 Part 1
Process file with two passes:
1. Extract initial numbers array and operators array
2. Process remaining lines by applying operators to update numbers
"""

def read_file(filename):
    """Read the file and return all lines"""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse_line_to_numbers(line):
    """Parse a line of space-separated items into a list of integers"""
    return [int(x) for x in line.split()]

def parse_line_to_operators(line):
    """Parse a line of space-separated operators into a list of characters"""
    return list(line.split())

def is_operator_line(line):
    """Check if a line contains operators (+ or *) instead of numbers"""
    # Check if the first non-whitespace character is + or *
    items = line.split()
    if items and (items[0] == '+' or items[0] == '*'):
        return True
    return False

def main():
    lines = read_file('day6.txt')

    # First pass: Read numbers array and operators array
    numbers = None
    operators = None
    operator_line_index = -1

    for i, line in enumerate(lines):
        if i == 0:
            # First line is the numbers array
            numbers = parse_line_to_numbers(line)
        elif is_operator_line(line):
            # Found the operator line
            operators = parse_line_to_operators(line)
            operator_line_index = i
            break

    # Second pass: Process the lines between first line and operator line
    for i in range(1, operator_line_index):
        line = lines[i]
        current_numbers = parse_line_to_numbers(line)

        # For each position, apply the operator to combine numbers[j] with current_numbers[j]
        for j in range(len(numbers)):
            if operators[j] == '+':
                numbers[j] = numbers[j] + current_numbers[j]
            elif operators[j] == '*':
                numbers[j] = numbers[j] * current_numbers[j]

    # Calculate and print the sum
    result = sum(numbers)
    print(result)

if __name__ == '__main__':
    main()
