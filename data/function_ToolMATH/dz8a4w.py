def factorial_ap(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
