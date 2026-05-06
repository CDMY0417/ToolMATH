def solve_geometric_sequence(first_term: int, given_term: int, given_position: int, target_position: int):
    r = (given_term / first_term) ** (1 / (given_position - 1))
    nth_term = first_term * r ** (target_position - 1)
    return int(nth_term)
