def product_of_digits(n: int) -> int:
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product
