def largest_divisible_below(number: int, divisor: int):
    remainder = number % divisor
    return number - remainder
