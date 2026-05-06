def sum_powers_of_two(exponents: list[int]) -> int:
    return sum(2 ** k for k in exponents)
