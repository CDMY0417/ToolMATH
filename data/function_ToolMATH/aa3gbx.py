def sum_of_cubes_of_digits(number: int) -> int:
    return sum(int(digit) ** 3 for digit in str(number))
