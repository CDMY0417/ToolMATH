def ceiling_of_number_b(integer_part: int, fractional_part: float) -> int:
    if fractional_part > 0:
        return integer_part + 1
    else:
        return integer_part
