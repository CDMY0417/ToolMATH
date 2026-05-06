def divisors_count(n: int) -> int:
    count = 1
    factor = 2
    while n >= factor * factor:
        power = 0
        while n % factor == 0:
            power += 1
            n //= factor
        count *= (power + 1)
        factor += 1
    if n > 1:
        count *= 2
    return count
