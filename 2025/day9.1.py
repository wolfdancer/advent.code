from year2025.day9 import Position, Rectangle, parse_sorted_positions


def find_largest_rectangle(positions):
    """
    Find the pair of positions that creates the rectangle with the largest area.

    Optimized solution with early pruning:
    1. Positions are already sorted by row
    2. Pre-compute global column min/max for pruning (O(n))
    3. For each position, check others with early termination (O(n²) worst case,
       but significantly faster in practice due to pruning)

    Optimization strategies:
    - Early termination when remaining row distance can't beat current max
    - Sorted order allows skipping positions once area can't improve
    - Pre-computed column bounds avoid repeated calculations

    Time complexity: O(n²) worst case, but much faster in practice
    Space complexity: O(n)
    """
    if len(positions) < 2:
        return None

    # Positions are already sorted by row coordinate
    sorted_positions = positions

    # Pre-compute global column bounds for pruning
    min_col = min(p.column for p in positions)
    max_col = max(p.column for p in positions)
    max_col_dist = max_col - min_col + 1

    max_area = 0
    best_rectangle = None

    # For each position, check all positions after it in sorted order
    for i in range(len(sorted_positions)):
        # Maximum possible row distance from this position
        max_possible_row_dist = sorted_positions[-1].row - sorted_positions[i].row + 1

        # Early termination: if we can't possibly beat the current max area
        # even with the maximum possible column distance, we can stop
        if max_possible_row_dist * max_col_dist <= max_area:
            break

        for j in range(i + 1, len(sorted_positions)):
            rect = Rectangle(sorted_positions[i], sorted_positions[j])
            if rect.area > max_area:
                max_area = rect.area
                best_rectangle = rect

    return best_rectangle


def main():
    positions = parse_sorted_positions('day9.txt')
    largest_rect = find_largest_rectangle(positions)

    if largest_rect:
        print(largest_rect.area)
    else:
        print("No valid rectangle found")


if __name__ == '__main__':
    main()
