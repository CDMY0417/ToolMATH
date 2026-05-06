def power_of_power_h(base: int, exp1: int, exp2: int) -> int:
    inner_power = exp1 ** exp2
    return base ** inner_power
