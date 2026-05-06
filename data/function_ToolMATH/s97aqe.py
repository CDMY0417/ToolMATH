def factorial_gz(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
