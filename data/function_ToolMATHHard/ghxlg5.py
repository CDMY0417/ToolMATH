def solve_base_addition(a_str: str, b_str: str, s_str: str):
    """Return base h satisfying a+b=s in base h."""
    # Search h from max digit+1 to 20
    digits = [int(ch) for ch in a_str + b_str + s_str if ch.isdigit()]
    start = max(digits) + 1
    for h in range(start, 50):
        if int(a_str, h) + int(b_str, h) == int(s_str, h):
            return h
    return None
