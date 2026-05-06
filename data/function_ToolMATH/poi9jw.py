def count_rectangles_of_size(width: int, height: int, grid_width: int, grid_height: int) -> int:
    return (grid_width - width + 1) * (grid_height - height + 1)
