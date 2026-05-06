def has_same_digits(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))
