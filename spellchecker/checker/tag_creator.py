from spellchecker.checker import n_grams

NGRAMS = {1: n_grams.ALPH,
          2: n_grams.BIGRAMS,
          3: n_grams.TRIGRAMS,
          4: n_grams.FOURGRAMS}


def make_full_tag(word: str) -> str:
    spell_tag = ''
    position = 0
    length = len(word)
    while position != length:
        for number in [4, 3, 2, 1]:
            spell_tag, position, done = make_part_tag(spell_tag, word,
                                                      position, number, length)
            if done or position == length:
                break
    return spell_tag


def make_part_tag(spell_tag: str, word: str, position: int, number: int,
                  length: int) -> (str, int, bool):
    tag = find_gram(word, position, number, length)
    if tag is None:
        return spell_tag, position, False
    else:
        spell_tag += tag
        position += number
        return spell_tag, position, True


def find_gram(word: str, position: int, number: int, length: int) -> str:
    if position <= length - number:
        word_part = word[position: position + number]
        if number != 1 and word_part == word[position] * number:
            return word[position]
        else:
            return NGRAMS.get(number).get(word_part)
