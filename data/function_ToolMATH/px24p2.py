def product_of_integers_b(numbers: list[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product
