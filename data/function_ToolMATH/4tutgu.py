def integer_root_theorem_candidates(constant_term: int):
    divisors = set()
    for i in range(1, int(abs(constant_term) ** 0.5) + 1):
        if constant_term % i == 0:
            divisors.add(i)
            divisors.add(-i)
            divisors.add(constant_term // i)
            divisors.add(-(constant_term // i))
    return sorted(divisors)
