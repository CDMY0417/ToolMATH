def remainder_of_product(numbers: list[int], divisor: int) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product % divisor
