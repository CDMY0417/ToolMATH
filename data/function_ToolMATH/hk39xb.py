def describe_intervals_with_sign(signs: list[str], intervals: list[any], desired_sign: str):
    solution_intervals = []
    for sign, interval in zip(signs, intervals):
        if sign == desired_sign:
            solution_intervals.append(interval)
    return solution_intervals
