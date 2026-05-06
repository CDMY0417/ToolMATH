def unit_conversion(from_unit_value: float, to_unit_value: float, amount: float):
    conversion_rate = from_unit_value / to_unit_value
    return amount * conversion_rate
