def count_divisors_d(n: int) -> int:
    count = 1
    d = 2
    while d * d <= n:
        current_count = 0
        while n % d == 0:
            n //= d
            current_count += 1
        count *= (current_count + 1)
        d += 1
    if n > 1:
        count *= 2
    return count
