def horizontal_asymptote_degree_rule(degree_num: int, degree_den: int):
    if degree_num < degree_den:
        return 0
    elif degree_num == degree_den:
        return 'approach leading coefficient ratio'
    else:
        return 'no horizontal asymptote'
