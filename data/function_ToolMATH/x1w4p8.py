def adjust_dimensions_by_margins(original_length: float, original_width: float, margin: float) -> tuple:
    adjusted_length = original_length - 2 * margin
    adjusted_width = original_width - 2 * margin
    return adjusted_length, adjusted_width
