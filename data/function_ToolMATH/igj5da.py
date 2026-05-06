def double_factorial_odd(n: int) -> int:
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result
