def count_elements_less_than(elements: list[int], limit: int) -> int:
    return len([x for x in elements if x < limit])
