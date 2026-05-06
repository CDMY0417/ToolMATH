def calculate_product_probability(numerators: list[int], denominators: list[int]) -> tuple:
    product_numerator = 1
    product_denominator = 1
    for n, d in zip(numerators, denominators):
        product_numerator *= n
        product_denominator *= d
    return product_numerator, product_denominator
