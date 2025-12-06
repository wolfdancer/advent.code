#!/usr/bin/env python3
"""Analyze the example to understand the pattern"""

example = """123 328  51 64
 45 64  387 23
  6 98  215 314"""

lines = example.split('\n')

print("Original lines:")
for i, line in enumerate(lines):
    print(f"Line {i}: '{line}'")

print("\nCharacter positions (0-indexed):")
max_len = max(len(line) for line in lines)
for i, line in enumerate(lines):
    print(f"Line {i}: ", end='')
    for j, char in enumerate(line):
        print(f"{j}:{char} ", end='')
    print()

print(f"\nMax line length: {max_len}")

print("\nReading character-by-character, right-to-left by column:")
for col_idx in range(max_len - 1, -1, -1):
    chars = []
    for line in lines:
        if col_idx < len(line):
            chars.append(line[col_idx])
        else:
            chars.append(' ')
    print(f"Column {col_idx}: {chars} -> '{''.join(chars)}'")

print("\nExpected problems (from description):")
print("Rightmost: 4 + 431 + 623 = 1058")
print("Second from right: 175 * 581 * 32 = 3253600")
print("Third from right: 8 + 248 + 369 = 625")
print("Leftmost: 356 * 24 * 1 = 8544")
