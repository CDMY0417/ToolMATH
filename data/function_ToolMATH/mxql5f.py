def count_divisors_in_range_a(n: int, lo: int, hi: int) -> int:
    count = 0
    for i in range(lo, hi + 1):
        if n % i == 0:
            count += 1
    return count
