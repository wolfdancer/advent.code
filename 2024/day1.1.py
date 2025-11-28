def solve_part1(filename):
    # Read the file and parse the two lists
    left_list = []
    right_list = []

    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the sum of absolute differences
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance


if __name__ == "__main__":
    result = solve_part1("day1.txt")
    print(f"Total distance: {result}")
