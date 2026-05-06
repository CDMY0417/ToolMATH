def product_of_list_f(numbers: list[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product
