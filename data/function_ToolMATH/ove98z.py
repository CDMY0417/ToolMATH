def convert_currency_to_farthings(pounds: int, shillings: int, pence: int) -> int:
    farthings_per_pence = 4
    pence_per_shilling = 12
    shillings_per_pound = 20
    total_farthings = (pounds * shillings_per_pound * pence_per_shilling * farthings_per_pence) + (shillings * pence_per_shilling * farthings_per_pence) + (pence * farthings_per_pence)
    return total_farthings
