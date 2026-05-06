def possible_rectangle_positions(rows: int, columns: int, rect_height: int, rect_width: int) -> int:
    return (rows - rect_height + 1) * (columns - rect_width + 1)
