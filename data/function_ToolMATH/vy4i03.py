def determine_rounding_effect(number: float, place: int) -> str:
    digit = int(number * (10 ** place)) % 10
    return 'round up' if digit >= 5 else 'round down'
