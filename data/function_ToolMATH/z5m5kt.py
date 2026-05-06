def units_digit_of_power_i(base: int, exponent: int) -> int:
    unit_digit_cycle = []
    current_unit_digit = 1
    seen_units = {}
    for i in range(exponent + 1):
        current_unit_digit = (current_unit_digit * base) % 10
        if current_unit_digit in seen_units:
            break
        unit_digit_cycle.append(current_unit_digit)
        seen_units[current_unit_digit] = i
    cycle_length = len(unit_digit_cycle)
    position_in_cycle = (exponent - 1) % cycle_length
    return unit_digit_cycle[position_in_cycle]
