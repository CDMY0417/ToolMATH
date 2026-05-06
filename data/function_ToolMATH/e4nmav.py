def multiply_and_square_root(numbers: list[float]) -> float:
    product = 1
    for number in numbers:
        product *= number
    return product ** 0.5
