def product_of_numbers_c(numbers: list[float]) -> float:
    product = 1
    for num in numbers:
        product *= num
    return product
