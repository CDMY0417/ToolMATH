def product_of_divisors(divisors: list[int]) -> int:
    product = 1
    for d in divisors:
        product *= d
    return product
