def count_switches(sequence: str) -> dict:
    switches = {'HT': 0, 'TH': 0, 'HH': 0, 'TT': 0}
    for i in range(len(sequence) - 1):
        pair = sequence[i:i+2]
        if pair in switches:
            switches[pair] += 1
    return switches
