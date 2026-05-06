def round_to_nearest_ten_a(number: int) -> int:
    remainder = number % 10
    if remainder < 5:
        return number - remainder
    else:
        return number + (10 - remainder)
