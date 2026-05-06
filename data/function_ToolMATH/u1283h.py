def arrange_in_descending_order(digits: list[int]) -> int:
    return int(''.join(sorted(map(str, digits), reverse=True)))
