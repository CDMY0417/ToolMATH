def count_arrangements_indistinguishable_boxes(ball_distribution: list[int]) -> int:
    from math import factorial
    unique = factorial(len(ball_distribution))
    buckets_count = {x: ball_distribution.count(x) for x in set(ball_distribution)}
    for count in buckets_count.values():
        unique //= factorial(count)
    return unique
