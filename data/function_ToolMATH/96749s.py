def calculate_individual_shares(shares: list[int], items_per_share: int):
    return [share * items_per_share for share in shares]
