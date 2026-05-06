def number_of_divisors_a(integer: int) -> int:
    from math import isqrt
    count = 0
    for i in range(1, isqrt(integer) + 1):
        if integer % i == 0:
            count += 1 if i * i == integer else 2
    return count
