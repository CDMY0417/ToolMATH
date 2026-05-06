def find_repeating_sequence(decimal: str) -> str:
    if '(' in decimal:
        start = decimal.index('(')
        end = decimal.index(')')
        return decimal[start+1:end]
    return ''
