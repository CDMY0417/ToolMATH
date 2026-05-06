def sum_of_divisors_d(prime_factors: list):
    total_sum = 1
    for base, exponent in prime_factors:
        total_sum *= sum([base**i for i in range(exponent + 1)])
    return total_sum
