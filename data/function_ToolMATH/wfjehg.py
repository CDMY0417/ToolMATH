def probability_common_fraction(successes: int, total_possibilities: int):
    from math import gcd
    g = gcd(successes, total_possibilities)
    return (successes // g, total_possibilities // g)
