def calculate_ones_digit_exponent(base_cycle: list[int], exponent: int) -> int:
    cycle_length = len(base_cycle)
    remainder = exponent % cycle_length
    return base_cycle[remainder - 1]
