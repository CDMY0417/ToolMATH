def find_periodic_sequence_term(initial_term: int, period: int, position: int) -> int:
    return (position - 1) % period + initial_term
