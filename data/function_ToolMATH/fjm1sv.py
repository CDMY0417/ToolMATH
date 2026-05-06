def modular_exponentiation_pattern(base: int, modulo: int, limit: int):
    seen = {}
    pattern = []
    current_value = 1
    for exponent in range(limit):
        if current_value in seen:
            cycle_start = seen[current_value]
            return pattern[cycle_start:]
        seen[current_value] = exponent
        pattern.append(current_value)
        current_value = (current_value * base) % modulo
    return pattern
