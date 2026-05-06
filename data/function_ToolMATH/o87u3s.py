def find_repeating_cycle_length(base: int, mod: int) -> int:
    seen_remainders = {}
    value = base % mod
    count = 1
    while value not in seen_remainders:
        seen_remainders[value] = count
        value = (value * base) % mod
        count += 1
    return count - seen_remainders[value]
