def prime_factorization_of_factorial(n: int) -> dict:
    from collections import defaultdict
    def prime_factors(num):
        i = 2
        factors = defaultdict(int)
        while i * i <= num:
            while (num % i) == 0:
                factors[i] += 1
                num //= i
            i += 1
        if num > 1:
            factors[num] += 1
        return factors

    total_factors = defaultdict(int)
    for i in range(2, n + 1):
        factors = prime_factors(i)
        for prime, count in factors.items():
            total_factors[prime] += count
    return dict(total_factors)
