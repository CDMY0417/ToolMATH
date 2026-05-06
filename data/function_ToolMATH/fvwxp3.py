def product_of_series(numbers: list[float]) -> float:
    product = 1
    for number in numbers:
        product *= number
    return product
