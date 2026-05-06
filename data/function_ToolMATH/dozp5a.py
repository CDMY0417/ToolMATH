def largest_power_of_2_in_factorial(n: int) -> int:
    power = 0
    k = 2
    while k <= n:
        power += n // k
        k *= 2
    return power
