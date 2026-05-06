def possible_values_of_d(upper_limit: int):
    possible_d = []
    for d in range(2, upper_limit + 1, 2):
        possible_d.append(d)
    return possible_d
