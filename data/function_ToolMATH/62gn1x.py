def power_units_digit(base: int, power: int) -> int:
    return (base % 10) ** (power % 4) % 10
