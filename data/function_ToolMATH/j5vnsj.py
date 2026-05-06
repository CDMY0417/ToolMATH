def list_all_outcomes(keiko_tosses: int, ephraim_tosses: int) -> list:
    from itertools import product
    keiko_outcomes = [''.join(outcome) for outcome in product('HT', repeat=keiko_tosses)]
    ephraim_outcomes = [''.join(outcome) for outcome in product('HT', repeat=ephraim_tosses)]
    return list(product(keiko_outcomes, ephraim_outcomes))
