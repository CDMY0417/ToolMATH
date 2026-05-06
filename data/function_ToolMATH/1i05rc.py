def largest_power_dividing_factorial(n: int, p: int) -> int:
    power = 0
    while n >= p:
        n //= p
        power += n
    return power
