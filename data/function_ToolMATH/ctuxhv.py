def units_digit_of_product_a(numbers: list[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product % 10
