def calculate_inner_dimension(outer_length: int, outer_width: int, border_width: int) -> tuple:
    inner_length = outer_length - 2 * border_width
    inner_width = outer_width - 2 * border_width
    return inner_length, inner_width
