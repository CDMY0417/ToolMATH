def round_to_nearest_ten_thousand(number: int) -> int:
    remainder = number % 10000
    if remainder >= 5000:
        return number + (10000 - remainder)
    else:
        return number - remainder
