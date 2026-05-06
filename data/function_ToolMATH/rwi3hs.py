def compute_lcm_a(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result
