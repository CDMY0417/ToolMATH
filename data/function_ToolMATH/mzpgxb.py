def product_of_ways(ways: list[int]) -> int:
    product = 1
    for way in ways:
        product *= way
    return product
