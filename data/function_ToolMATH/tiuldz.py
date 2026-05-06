def is_relatively_prime_d(a: int, b: int) -> bool:
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return gcd(a, b) == 1
