def sum_of_powers_a(bases: list[int], exponent: int) -> int:
    return sum(base ** exponent for base in bases)
