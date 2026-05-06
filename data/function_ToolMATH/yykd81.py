def calculate_segment_from_ratio(known_side_1: float, known_side_2: float, total_length_1: float) -> float:
    segment_length = (known_side_1 / known_side_2) * total_length_1
    return segment_length
