def digit_sum_equals_target(target: int):
    result = []
    for tens in range(1, 10):
        for units in range(0, 10):
            if tens + units == target:
                result.append(tens * 10 + units)
    return result
