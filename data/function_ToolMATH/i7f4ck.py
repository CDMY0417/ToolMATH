def possible_rational_roots(constant_divisors: set, leading_coef_divisors: set) -> set:
    roots = set()
    for a in constant_divisors:
        for b in leading_coef_divisors:
            roots.add(a / b)
            roots.add(-a / b)
    return roots
