def lex_position_of_word(word: str, alphabet: str):
    # 1-based lex position of word over alphabet
    base = len(alphabet)
    index = 0
    for ch in word:
        index = index*base + alphabet.index(ch)
    return index + 1
