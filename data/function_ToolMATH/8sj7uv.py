def count_fibonacci_based_numbers(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    a, b = 2, 3
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
