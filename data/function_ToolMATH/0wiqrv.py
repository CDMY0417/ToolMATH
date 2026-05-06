def largest_n_digit_in_base(n: int, base: int) -> int:
    smallest_next_digit = base ** n
    largest_n_digit_number = smallest_next_digit - 1
    return largest_n_digit_number
