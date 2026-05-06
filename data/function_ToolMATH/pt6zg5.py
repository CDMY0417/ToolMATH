def find_repeating_term_at_position(pos: int, period: int, sequence: list):
    return sequence[(pos - 1) % period]
