def modular_repeat_cycle(base: int, modulus: int) -> int:
    current = base
    count = 1
    seen_values = {current}
    while True:
        current = (current * base) % modulus
        if current in seen_values:
            break
        seen_values.add(current)
        count += 1
    return count
