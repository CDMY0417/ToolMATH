def elements_in_union(a: int, b: int, intersection: int) -> int:
    return (a - intersection) + (b - intersection) + intersection
