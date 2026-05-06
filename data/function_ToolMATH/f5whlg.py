def largest_multiple_less_than_b(multiple: int, limit: int) -> int:
    quotient = limit // multiple
    return multiple * quotient
