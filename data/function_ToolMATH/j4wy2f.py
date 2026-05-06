def denominator_collapse(exponents: list[int]) -> int:
    product = 1
    for exp in exponents:
        product *= (5**exp + 1)
    return 4 * product
