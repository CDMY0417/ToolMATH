def units_digit_cycle(base: int):
    seen_digits = set()
    cycle = []
    n = 1
    while True:
        units_digit = (base ** n) % 10
        if units_digit in seen_digits:
            break
        cycle.append(units_digit)
        seen_digits.add(units_digit)
        n += 1
    return cycle
