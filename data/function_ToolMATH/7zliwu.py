def product_of_numbers_b(numbers: list[float]) -> float:
    product = 1
    for number in numbers:
        product *= number
    return product
