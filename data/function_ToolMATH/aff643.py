def least_positive_solution_to_congruences(remainder1: int, modulus1: int, remainder2: int, modulus2: int) -> int:
    n = remainder1
    while n % modulus2 != remainder2:
        n += modulus1
    return n
