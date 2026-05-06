def even_and_not_multiple_of_three(a: int, b: int) -> bool:
    product = a * b
    return (product % 2 == 0) and (product % 3 != 0)
