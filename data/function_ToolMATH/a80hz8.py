def product_of_digits_a(number: int) -> int:
    if number == 0:
        return 0
    product = 1
    while number > 0:
        product *= number % 10
        number //= 10
    return product
