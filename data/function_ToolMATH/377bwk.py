def inverse_sequence_element(n: int, t1: float, t2: float) -> float:
    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        t_prev_2, t_prev_1 = t1, t2
        for _ in range(3, n + 1):
            t_current = t_prev_1 + t_prev_2
            t_prev_2, t_prev_1 = t_prev_1, t_current
        return t_current
