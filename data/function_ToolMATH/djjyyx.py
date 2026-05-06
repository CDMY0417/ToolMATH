def find_smallest_integer_ending_in_digit_divisible_by(digit: int, divisor: int) -> int:
    num = digit
    while num % divisor != 0:
        num += 10
    return num
