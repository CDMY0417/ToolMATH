def calculate_gcd_a(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
