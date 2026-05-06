def simplify_sqrt_fraction(numerators: list[float], denominators: list[float]) -> float:
    from math import prod, sqrt
    # Convert all square roots to their simplest form
    num_product = prod([sqrt(x) for x in numerators])
    den_product = prod([sqrt(x) for x in denominators])
    # Simplify the fraction
    fraction_value = num_product / den_product
    return fraction_value
