from fractions import Fraction

def convert_minutes_to_mixed_hours(minutes: int) -> str:
    hours = minutes // 60
    remaining_minutes = minutes % 60
    mixed_number = Fraction(remaining_minutes, 60)
    return f'{hours} {mixed_number}'
