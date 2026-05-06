def fourth_powers_below(max_limit: int):
    result = []
    n = 1
    while (power := n**4) < max_limit:
        result.append(power)
        n += 1
    return result
