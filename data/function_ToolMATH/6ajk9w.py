def fibonacci_modulo(n: int, mod: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b
