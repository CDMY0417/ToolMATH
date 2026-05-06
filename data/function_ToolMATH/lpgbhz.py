def filter_multiples_of(lst: list[int], multiple: int) -> list[int]:
    return [x for x in lst if x % multiple == 0]
