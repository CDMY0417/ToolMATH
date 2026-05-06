def count_irreducible_factors_xn_minus_1(n: int):
    # Number of cyclotomic factors equals number of divisors of n
    count = 0
    for d in range(1, n+1):
        if n % d == 0:
            count += 1
    return count
