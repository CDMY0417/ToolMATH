def filter_divisors_by_factor(divisors: list[int], factor: int) -> list[int]:
    return [d for d in divisors if d % factor == 0]
