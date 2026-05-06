def highest_power_dividing_factorial(n: int, base: int) -> int:
    def prime_factors(x):
        i = 2
        factors = {}
        while i * i <= x:
            while (x % i) == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors[i] = 1
                x //= i
            i += 1
        if x > 1:
            factors[x] = 1
        return factors

    base_factors = prime_factors(base)
    min_power = float('inf')
    for prime, count in base_factors.items():
        power = 0
        k = prime
        while k <= n:
            power += n // k
            k *= prime
        min_power = min(min_power, power // count)
    return min_power
