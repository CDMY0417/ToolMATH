def check_relatively_prime(a: int, b: int) -> bool:
    def gcd(x: int, y: int) -> int:
        while y != 0:
            x, y = y, x % y
        return x
    return gcd(a, b) == 1
