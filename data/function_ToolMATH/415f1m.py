def differences_with_max_element(values: set) -> list:
    max_value = max(values)
    return [max_value - v for v in values if v != max_value]
