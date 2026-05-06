def convert_units_chain_ratio(a: float, b: float, c: float, d: float, target: float):
    """Return number of first units equal to target of fourth units."""
    # a U1 = b U2; c U2 = d U3
    # 1 U1 = b/a U2; 1 U2 = d/c U3 => 1 U1 = (b/a)*(d/c) U3
    u1_in_u3 = (b/a)*(d/c)
    return target / u1_in_u3
