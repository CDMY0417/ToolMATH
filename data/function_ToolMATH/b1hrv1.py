def sum_of_divisors(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total
