def square_pyramid_base_area(diagonal_length: float) -> float:
    import math
    side_length = diagonal_length / math.sqrt(2)
    return side_length**2
