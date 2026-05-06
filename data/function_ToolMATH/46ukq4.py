def product_modulo(numbers: list[int], modulus: int) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product % modulus
