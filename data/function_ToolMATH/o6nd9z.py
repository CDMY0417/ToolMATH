def greatest_multiple_below(limit: int, multiple_of: int) -> int:
    return limit - (limit % multiple_of)
