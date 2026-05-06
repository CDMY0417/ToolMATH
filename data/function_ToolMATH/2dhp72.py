def rational_roots(constant_divisors: set, leading_divisors: set):
    roots = set()
    for a in constant_divisors:
        for b in leading_divisors:
            roots.update({a / b, -a / b})
    return roots
