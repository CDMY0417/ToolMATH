def sum_of_repeat_elements(elements: list[int]) -> int:
    unique_elements = set(elements)
    return sum(el * elements.count(el) for el in unique_elements)
