def is_power_int(base: int, target: int) -> bool:
    if target <= 0 or base <= 1:
        return False
    x = 0
    power = 1
    while power < target:
        x += 1
        power *= base
    return power == target
