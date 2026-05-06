def smallest_power_of_two_exceeding(number: int) -> int:
    power = 0
    while (1 << power) < number:
        power += 1
    return power
