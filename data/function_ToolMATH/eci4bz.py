def factorial_as(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
