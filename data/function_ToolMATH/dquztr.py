def arrangements_around_circle(n: int) -> int:
    if n <= 1:
        return 1
    from math import factorial
    return factorial(n - 1)
