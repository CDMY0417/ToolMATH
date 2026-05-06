def min_number_of_digits_for_conditions(digit: int, divisor: int) -> int:
    count = 0
    while True:
        count += 1
        if (digit * count) % divisor == 0:
            return count
