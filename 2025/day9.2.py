from year2025.day9 import Position, Rectangle, parse_sorted_positions, check_valid_tiles


def build_valid_tiles(positions):
    """
    Build a map of valid tiles where each row maps to a range of columns.

    Args:
        positions: List of Position objects

    Returns:
        dict: Map of row -> range of columns
    """
    valid_tiles = {}

    for pos in positions:
        row = pos.row
        column = pos.column

        if row not in valid_tiles:
            # First position for this row
            valid_tiles[row] = range(column, column + 1)
        else:
            # Extend the range to include this column
            current_range = valid_tiles[row]
            min_col = min(current_range.start, column)
            max_col = max(current_range.stop - 1, column)
            valid_tiles[row] = range(min_col, max_col + 1)

    return valid_tiles


def build_vertical_tiles(positions):
    """
    Build a map of vertical tiles where each column maps to a range of rows.

    Args:
        positions: List of Position objects

    Returns:
        dict: Map of column -> range of rows
    """
    vertical_tiles = {}

    for pos in positions:
        row = pos.row
        column = pos.column

        if column not in vertical_tiles:
            # First position for this column
            vertical_tiles[column] = range(row, row + 1)
        else:
            # Extend the range to include this row
            current_range = vertical_tiles[column]
            min_row = min(current_range.start, row)
            max_row = max(current_range.stop - 1, row)
            vertical_tiles[column] = range(min_row, max_row + 1)

    return vertical_tiles


def extend_valid_tiles(valid_tiles, vertical_tiles):
    """
    Extend valid_tiles ranges based on vertical_tiles to fill in gaps.

    Args:
        valid_tiles: dict mapping row -> range of columns
        vertical_tiles: dict mapping column -> range of rows

    Returns:
        dict: Updated valid_tiles map
    """
    for column, row_range in vertical_tiles.items():
        for row in row_range:
            if row not in valid_tiles:
                # Create a new entry for this row
                valid_tiles[row] = range(column, column + 1)
            else:
                # Check if the column is in the range
                current_range = valid_tiles[row]
                if column < current_range.start or column >= current_range.stop:
                    # Extend the range to include this column
                    min_col = min(current_range.start, column)
                    max_col = max(current_range.stop - 1, column)
                    valid_tiles[row] = range(min_col, max_col + 1)

    return valid_tiles


def find_largest_valid_rectangle(positions, valid_tiles):
    """
    Find the largest valid rectangle from the positions.

    Args:
        positions: List of Position objects
        valid_tiles: dict mapping row -> range of columns

    Returns:
        Rectangle: The largest valid rectangle
    """
    max_area = 0
    best_rectangle = None

    # Check all pairs of positions
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            rect = Rectangle(positions[i], positions[j])
            if check_valid_tiles(valid_tiles, rect):
                if rect.area > max_area:
                    max_area = rect.area
                    best_rectangle = rect

    return best_rectangle, max_area


def main():
    # Parse positions from input file
    positions = parse_sorted_positions('day9.txt')

    # Build valid_tiles map (row -> column range)
    valid_tiles = build_valid_tiles(positions)

    # Build vertical_tiles map (column -> row range)
    vertical_tiles = build_vertical_tiles(positions)

    # Extend valid_tiles based on vertical_tiles
    valid_tiles = extend_valid_tiles(valid_tiles, vertical_tiles)

    # Find the largest valid rectangle
    largest_rect, max_area = find_largest_valid_rectangle(positions, valid_tiles)

    # Print the answer
    print(max_area)


if __name__ == '__main__':
    main()
