import sys
sys.path.insert(0, '.')
from day3.1 import identify_max_joltage

# Test with example data
test_cases = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

total = 0
for line in test_cases:
    result = identify_max_joltage(line)
    print(f"{line} -> {result}")
    total += result

print(f"\nTotal: {total}")
