def count_divisions_by_factor(n: int, factor: int) -> int:
    count = 0
    while n % factor == 0:
        n //= factor
        count += 1
    return count
