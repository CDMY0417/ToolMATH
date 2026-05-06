def modular_product_a(numbers: list[int], mod: int) -> int:
    product = 1
    for num in numbers:
        product *= num
        product %= mod
    return product
