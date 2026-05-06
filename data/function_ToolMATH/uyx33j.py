def power_of_base_b_equals_a(a: int, b: int):
    n = 0
    current_power = 1
    while current_power < a:
        n += 1
        current_power *= b
    if current_power == a:
        return n
    else:
        return None
