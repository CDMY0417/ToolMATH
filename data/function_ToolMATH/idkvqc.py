def are_lines_parallel_b(direction_vector1: tuple[int, int], direction_vector2: tuple[int, int]) -> bool:
    return direction_vector1[0] * direction_vector2[1] == direction_vector1[1] * direction_vector2[0]
