def apply_am_gm_inequality_c(numbers: list[float]) -> float:
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers))
