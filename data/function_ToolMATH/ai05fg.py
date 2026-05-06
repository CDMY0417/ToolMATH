def create_alternating_sequence(start: int, end: int, step: int):
    sequence = []
    sign = 1
    for i in range(start, end + 1, step):
        sequence.append(sign * i)
        sign *= -1
    return sequence
