def sum_of_digits_c(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
