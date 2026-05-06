def compute_gcd_from_exponents(bases: list[int], min_exponents: list[int]) -> int:
    gcd = 1
    for base, exp in zip(bases, min_exponents):
        gcd *= base ** exp
    return gcd
