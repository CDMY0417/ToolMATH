def gcd_lcm_relation(m: int, n: int) -> bool:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)
    return gcd(m, n) * lcm(m, n) == m * n
