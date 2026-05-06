def integer_roots_theorem_candidates(constant_coefficient: int):
    from sympy import divisors
    candidates = divisors(constant_coefficient) + [-d for d in divisors(constant_coefficient)]
    return candidates
