def product_of_solutions_a(numbers: list[float]) -> float:
    product = 1
    for number in numbers:
        product *= number
    return product
