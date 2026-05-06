def filter_divisors(number: int, candidates: list[int]) -> list[int]:
    return [x for x in candidates if number % x == 0]
