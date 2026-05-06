def total_remainder(group_count: int, remainder_per_group: int, divisor: int) -> int:
    total_remainder = group_count * remainder_per_group
    return total_remainder % divisor
