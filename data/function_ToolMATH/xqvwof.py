def sum_divisors_max(x: int, c: int) -> int:
    max_sum = float('-inf')
    for a in range(1, x + 1):
        if x % a == 0:
            b = x // a
            total = a + b + c
            if total > max_sum:
                max_sum = total
    return max_sum
