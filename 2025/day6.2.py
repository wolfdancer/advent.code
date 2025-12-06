#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6 Part 2
Process file reading right-to-left, character by character:
1. Read character columns from right to left
2. Group digits into numbers (separated by whitespace columns)
3. Apply operators to each problem (group of numbers)
4. Sum all results to get grand total
"""

def read_file(filename):
    """Read the file and return all lines"""
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]

def is_operator_line(line):
    """Check if a line contains operators (+ or *) instead of numbers"""
    items = line.split()
    if items and (items[0] == '+' or items[0] == '*'):
        return True
    return False

def extract_numbers_from_columns(lines, operator_line_index):
    """
    Read character columns right-to-left and extract numbers.
    Returns a list of number groups (one per problem/operator).
    """
    # Find the maximum line length
    max_len = max(len(line) for line in lines[:operator_line_index])

    # Read character columns from right to left
    char_columns = []
    for col_idx in range(max_len - 1, -1, -1):
        column_chars = []
        for line_idx in range(operator_line_index):
            line = lines[line_idx]
            if col_idx < len(line):
                column_chars.append(line[col_idx])
            else:
                column_chars.append(' ')
        char_columns.append(''.join(column_chars))

    # Group columns into numbers (separated by all-space columns)
    problems = []
    current_problem = []

    for col_str in char_columns:
        # Check if this column is all spaces
        if col_str.strip() == '':
            # End of current problem
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            # Extract digits from this column (ignore spaces)
            digits = col_str.replace(' ', '')
            if digits:
                current_problem.append(int(digits))

    # Don't forget the last problem
    if current_problem:
        problems.append(current_problem)

    return problems

def parse_operators(line):
    """Parse a line of space-separated operators into a list of characters"""
    return list(line.split())

def main():
    lines = read_file('day6.txt')

    # Find the operator line
    operator_line_index = -1
    operators = []

    for i, line in enumerate(lines):
        if is_operator_line(line):
            operators = parse_operators(line)
            operator_line_index = i
            break

    # Reverse operators to match right-to-left reading order
    operators = operators[::-1]

    # Extract problems (groups of numbers) from columns
    problems = extract_numbers_from_columns(lines, operator_line_index)

    # Process each problem with its operator
    problem_results = []
    for prob_idx, numbers in enumerate(problems):
        operator = operators[prob_idx]

        # Apply the operator to all numbers in the problem
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num

        problem_results.append(result)

    # Calculate grand total
    grand_total = sum(problem_results)
    print(grand_total)

if __name__ == '__main__':
    main()
