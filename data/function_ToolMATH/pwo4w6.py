def count_unique_digit_numbers(n: int) -> int:
    if n == 0:
        return 0
    product = 9
    for i in range(1, n):
        product *= 10 - i
    return product
