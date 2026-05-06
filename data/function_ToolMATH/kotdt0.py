def count_multiples_in_interval(number: int, start: int, end: int) -> int:
    first_multiple = (start + number - 1) // number * number
    last_multiple = end // number * number
    if first_multiple > end or last_multiple < start:
        return 0
    return (last_multiple - first_multiple) // number + 1
