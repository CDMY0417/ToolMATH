def count_trailing_zeroes_a(n: int) -> int:
    count = 0
    while n % 10 == 0 and n != 0:
        n //= 10
        count += 1
    return count
