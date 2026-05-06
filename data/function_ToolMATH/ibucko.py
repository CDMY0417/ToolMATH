def find_divisible_numbers(limit: int, divisor: int, congruence_mod: int, congruence_val: int) -> list:
    return [x for x in range(divisor, limit + 1, divisor) if x % congruence_mod == congruence_val]
