def find_repeating_remainder_cycle(base: int, divisor: int) -> int:
    seen_remainders = {}
    current_value = base % divisor
    cycle_length = 0
    while current_value not in seen_remainders:
        seen_remainders[current_value] = cycle_length
        cycle_length += 1
        current_value = (current_value * base) % divisor
    return cycle_length
