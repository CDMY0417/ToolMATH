def remove_fractions(lhs: str, rhs: str, multiplier: int):
    lhs_no_fractions = f"{multiplier}({lhs})"
    rhs_no_fractions = f"{multiplier}({rhs})"
    return lhs_no_fractions, rhs_no_fractions
