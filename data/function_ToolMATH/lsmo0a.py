def reverse_digits_a(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_number = int(str(abs(n))[::-1])
    return sign * reversed_number
