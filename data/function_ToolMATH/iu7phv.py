def least_common_multiple_of_primes(primes: list[int]) -> int:
    lcm = 1
    for prime in primes:
        lcm *= prime
    return lcm
