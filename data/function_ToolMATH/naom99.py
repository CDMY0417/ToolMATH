def simplify_factorial_fraction(numerator_factorials: list[int], denominator_factorials: list[int]) -> list[int]:
    simplified_factorials = []
    for num in numerator_factorials:
        if num in denominator_factorials:
            denominator_factorials.remove(num)
        else:
            simplified_factorials.append(num)
    for den in denominator_factorials:
        simplified_factorials.append(-den)
    return simplified_factorials
