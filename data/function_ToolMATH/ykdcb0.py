def has_unique_digits(number: int) -> bool:
    return len(set(str(number))) == len(str(number))
