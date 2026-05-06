def modular_exponentiation_cycle(base: int, mod: int):
    cycle = []
    current = base % mod
    while current not in cycle:
        cycle.append(current)
        current = (current * base) % mod
    return cycle
