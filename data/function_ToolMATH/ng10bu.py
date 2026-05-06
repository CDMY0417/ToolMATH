def odd_multiples(start: int, end: int, multiple: int) -> list:
    return [x for x in range(start, end + 1) if x % multiple == 0 and x % 2 != 0]
