def last_digits_of_divisibles(divisor: int) -> set:
    last_digits = set()
    for number in range(10):
        if number % divisor == 0:
            last_digits.add(number)
    return last_digits
