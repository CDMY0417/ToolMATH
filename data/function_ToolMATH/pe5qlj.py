def number_in_arithmetic_sequence(first_term1: int, common_difference1: int, first_term2: int, common_difference2: int, range_end: int) -> int:
    a = first_term1
    b = first_term2
    d1 = common_difference1
    d2 = common_difference2
    largest_common = None
    while a <= range_end:
        if a % d2 == b % d2:
            largest_common = a
        a += d1
    return largest_common if largest_common is not None else -1
