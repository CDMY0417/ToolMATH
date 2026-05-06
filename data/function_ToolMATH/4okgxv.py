def double_factorial_even(n: int) -> int:
    result = 1
    for i in range(n, 1, -2):
        result *= i
    return result
