def is_coprime(a: int, b: int):
    while b:
        a, b = b, a % b
    return a == 1
