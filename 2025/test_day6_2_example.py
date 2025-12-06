#!/usr/bin/env python3
"""Test day6.2.py with example data"""

def read_file(filename):
    """Read the file and return all lines"""
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f.readlines()]

def parse_numbers_by_column(lines, operator_line_index):
    """
    Parse numbers into columns, reading right-to-left.
    Returns a list of columns, where each column is a list of numbers from top to bottom.
    """
    # Split each line into tokens
    rows = []
    for i in range(operator_line_index):
        tokens = lines[i].split()
        rows.append(tokens)

    # Find the maximum number of columns
    max_cols = max(len(row) for row in rows)

    # Build columns from right to left
    columns = []
    for col_idx in range(max_cols - 1, -1, -1):  # Right to left
        column = []
        for row in rows:
            if col_idx < len(row):
                column.append(int(row[col_idx]))
        columns.append(column)

    return columns

def parse_operators(line):
    """Parse a line of space-separated operators into a list of characters"""
    return list(line.split())

def is_operator_line(line):
    """Check if a line contains operators (+ or *) instead of numbers"""
    items = line.split()
    if items and (items[0] == '+' or items[0] == '*'):
        return True
    return False

def main():
    lines = read_file('day6.example2.txt')

    # Find the operator line
    operator_line_index = -1
    operators = []

    for i, line in enumerate(lines):
        if is_operator_line(line):
            operators = parse_operators(line)
            operator_line_index = i
            break

    print(f"Operators (left to right): {operators}")

    # Reverse operators to match right-to-left column order
    operators = operators[::-1]
    print(f"Operators (right to left): {operators}")

    # Parse numbers into columns (right to left)
    columns = parse_numbers_by_column(lines, operator_line_index)

    print("\nColumns (right to left):")
    for i, col in enumerate(columns):
        print(f"Column {i}: {col}")

    # Process each column with its operator
    column_results = []
    for col_idx, column in enumerate(columns):
        operator = operators[col_idx]

        # Apply the operator to all numbers in the column
        if operator == '+':
            result = sum(column)
            print(f"\nColumn {col_idx} (operator '+'): {' + '.join(map(str, column))} = {result}")
        elif operator == '*':
            result = 1
            for num in column:
                result *= num
            print(f"\nColumn {col_idx} (operator '*'): {' * '.join(map(str, column))} = {result}")

        column_results.append(result)

    # Calculate grand total
    grand_total = sum(column_results)
    print(f"\nColumn results: {column_results}")
    print(f"Grand total: {' + '.join(map(str, column_results))} = {grand_total}")
    print(f"\nExpected: 3263827")

if __name__ == '__main__':
    main()
