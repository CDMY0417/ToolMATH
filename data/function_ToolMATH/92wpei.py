def count_non_multiples_in_range(multiple: int, limit: int) -> int:
    return limit - (limit // multiple)
