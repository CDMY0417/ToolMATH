def calculate_proportional_width(original_length: float, original_width: float, new_length: float) -> float:
    ratio = new_length / original_length
    new_width = original_width * ratio
    return new_width
