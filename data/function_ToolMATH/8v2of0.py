def potential_rational_roots(constant: int) -> list[int]:
    from itertools import chain
    divisors = set(chain.from_iterable((i, -i) for i in range(1, abs(constant) + 1) if constant % i == 0))
    return sorted(divisors)
