def product_of_powers_e(numbers: list[float], power: int) -> float:
    result = 1
    for number in numbers:
        result *= number ** power
    return result
