def find_repetitive_power_modulus(base: int, mod: int) -> int:
    seen = {}
    current = base % mod
    power = 1
    while current not in seen:
        seen[current] = power
        power += 1
        current = (current * base) % mod
    repeat_period = power - seen[current]
    return repeat_period
