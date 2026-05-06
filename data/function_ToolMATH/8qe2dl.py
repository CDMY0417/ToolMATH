def simplify_fraction_j(fraction: tuple[int, int]) -> tuple[int, int]:
    import math
    gcd = math.gcd(fraction[0], fraction[1])
    return (fraction[0] // gcd, fraction[1] // gcd)
