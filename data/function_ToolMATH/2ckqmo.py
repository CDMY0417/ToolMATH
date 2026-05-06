def count_multiples_g(multiple: int, start: int, end: int) -> int:
    return end // multiple - (start - 1) // multiple
