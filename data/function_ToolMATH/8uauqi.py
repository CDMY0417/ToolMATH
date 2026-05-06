def largest_number_divisible_by(digits: int, divisor: int) -> int:
    largest_number = 10**digits - 1
    while largest_number % divisor != 0:
        largest_number -= 1
    return largest_number
