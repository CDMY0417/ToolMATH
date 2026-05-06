def product_of_integers_d(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result
