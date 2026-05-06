def lcm_c(numbers: list[int]) -> int:
    from math import gcd
    def lcm_two(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)
    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm_two(lcm_result, number)
    return lcm_result
