def solve_arithmetic_sequence(known_terms: list[int], term_positions: list[int], position_to_find: int) -> int:
    a_2, a_4 = known_terms
    p_2, p_4 = term_positions
    d = (a_4 - a_2) // (p_4 - p_2)
    a_n = a_4 + (position_to_find - p_4) * d
    return a_n
