def lcm_d(numbers: list[int]) -> int:
    from math import gcd
    def lcm_two_numbers(x: int, y: int) -> int:
        return abs(x * y) // gcd(x, y)
    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm_two_numbers(current_lcm, number)
    return current_lcm
