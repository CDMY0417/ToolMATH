def largest_number_less_than_limit(numbers: list[int], limit: int) -> int:
    return max(n for n in numbers if n < limit)
