def power_modulo_cycle(base: int, modulus: int):
    seen = {}
    cycle = []
    power = 1
    while power not in seen:
        seen[power] = len(cycle)
        cycle.append(power)
        power = (power * base) % modulus
    return cycle
