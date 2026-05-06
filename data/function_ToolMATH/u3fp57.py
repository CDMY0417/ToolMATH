def integer_solutions_for_sum_of_squares(value: int) -> int:
    count = 0
    for x in range(int(value**0.5) + 1):
        y_squared = value - x**2
        y = int(y_squared**0.5)
        if y_squared == y**2:
            if x == 0 or y == 0:
                count += 2
            else:
                count += 4
    return count
