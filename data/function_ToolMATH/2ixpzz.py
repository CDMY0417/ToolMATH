def sum_of_factors(n: int) -> int:
    factor_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factor_sum += i
            if i != n // i:
                factor_sum += n // i
    return factor_sum
