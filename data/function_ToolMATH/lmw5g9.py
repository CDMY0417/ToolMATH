def cents_to_dollars_a(cents: int) -> str:
    dollars = cents // 100
    leftover_cents = cents % 100
    return f'${dollars}.{leftover_cents:02d}'
