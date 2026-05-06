def odd_or_multiple_of_three(a: int, b: int) -> bool:
    product = a * b
    return (product % 2 != 0) or (product % 3 == 0)
