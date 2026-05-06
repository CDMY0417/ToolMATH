def largest_number_in_base(base: int, num_digits: int) -> int:
    return (base - 1) * (base ** num_digits - 1) // (base - 1)
