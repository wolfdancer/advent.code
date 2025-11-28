# Read the input file
with open('day1.txt', 'r') as f:
    lines = f.readlines()

# Parse the two lists
left_list = []
right_list = []

for line in lines:
    parts = line.strip().split()
    left_list.append(int(parts[0]))
    right_list.append(int(parts[1]))

# Calculate the similarity score
total = 0

for num in left_list:
    # Count how many times this number appears in the right list
    count = right_list.count(num)
    # Multiply the number by its count and add to total
    total += num * count

print(total)
