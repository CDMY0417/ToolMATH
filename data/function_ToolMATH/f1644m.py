def ceil_sqrt(number: int) -> int:
    return int(number**0.5) + (1 if (int(number**0.5))**2 < number else 0)
