# Initialize variables
beams = set()
splits = 0

# Read the input file
with open('day7.txt', 'r') as f:
    lines = f.readlines()

# Process first line - find 'S' and add its index to beams
first_line = lines[0].rstrip('\n')
for i, char in enumerate(first_line):
    if char == 'S':
        beams.add(i)

# Process remaining lines
for line in lines[1:]:
    line = line.rstrip('\n')

    # Convert indices of '^' to a set
    splitters = {i for i, char in enumerate(line) if char == '^'}

    # Create next_beams set
    next_beams = set()

    # Iterate through all values in beams
    for beam in beams:
        if beam not in splitters:
            next_beams.add(beam)
            continue

        # Beam hit a splitter
        splits += 1

        # Add left beam (beam - 1) if valid
        if beam - 1 >= 0:
            next_beams.add(beam - 1)

        # Add right beam (beam + 1) if valid
        if beam + 1 < len(line):
            next_beams.add(beam + 1)

    # Update beams for next iteration
    beams = next_beams

# Print the result
print(splits)
