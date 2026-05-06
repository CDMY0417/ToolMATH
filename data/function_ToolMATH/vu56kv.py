def count_ways_to_form_even_divisor(exponents: dict[int, list[int]]) -> int:
    count = 1
    for p, possible_exponents in exponents.items():
        count *= len(possible_exponents)
    return count
