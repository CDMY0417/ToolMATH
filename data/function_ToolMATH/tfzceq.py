def sum_of_digits_ab(number: int) -> int:
    return sum(int(d) for d in str(number))
