def find_decimal_representation_cycle(n: int) -> str:
    from decimal import Decimal, getcontext
    getcontext().prec = 100  # Set precision high enough to detect cycles
    decimal_repr = str(Decimal(1) / Decimal(n))[2:]  # Remove '0.'
    for cycle_length in range(1, len(decimal_repr)):
        cycle = decimal_repr[:cycle_length]
        if cycle * (len(decimal_repr) // cycle_length) + cycle[:len(decimal_repr) % cycle_length] == decimal_repr:
            return cycle
    return ''
