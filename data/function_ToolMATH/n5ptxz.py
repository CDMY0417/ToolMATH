def same_number_of_heads(keiko_outcome: str, ephraim_outcome: str) -> bool:
    keiko_heads = keiko_outcome.count('H')
    ephraim_heads = ephraim_outcome.count('H')
    return keiko_heads == ephraim_heads
