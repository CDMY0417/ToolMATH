def distribute_terms_c(factor: str, terms: list[str]) -> list[str]:
    distributed = []
    for term in terms:
        distributed.append(f'{factor}*{term}')
    return distributed
