from year2025.day8 import read_positions_and_create_pairs

# Read and parse the input file
circuits, pairs = read_positions_and_create_pairs('day8.txt')

# Initialize num_circuits to the size of circuits
num_circuits = len(circuits)

# Loop through all items in pairs
for pair in pairs:
    # Get set from circuits using from_pos as the key
    from_circuit = circuits[pair.from_pos]
    # Get set from circuits using to_pos as the key
    to_circuit = circuits[pair.to_pos]

    # If from_circuit and to_circuit are not the same
    if from_circuit is not to_circuit:
        # If num_circuits is 2, calculate the product and break
        if num_circuits == 2:
            result = pair.from_pos.x * pair.to_pos.x
            print(result)
            break

        # Decrease num_circuits by 1
        num_circuits -= 1

        # Merge from_circuit and to_circuit into merged_circuit
        merged_circuit = from_circuit | to_circuit

        # Iterate through items on merged_circuit, update circuits
        for item in merged_circuit:
            circuits[item] = merged_circuit
