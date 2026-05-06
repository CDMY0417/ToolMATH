def largest_power_of_2_dividing_factorial(n: int) -> int:
    power = 0
    while n > 0:
        n //= 2
        power += n
    return power
