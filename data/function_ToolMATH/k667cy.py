def compute_factorial(n: int) -> int:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
