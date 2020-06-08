import re
from checker import n_grams, utils

NGRAMS = {1: n_grams.ALPH,
          2: n_grams.BIGRAMS,
          3: n_grams.TRIGRAMS,
          4: n_grams.FOURGRAMS}


def spell_checker(big_dict: dict, letter_dict: dict, word: str):
    correct = []
    word = word.lower()
    wrong_teg = make_tag(word)
    if big_dict.get(wrong_teg):
        words = utils.make_list(big_dict.get(wrong_teg))
        correct += words
    else:
        for teg in big_dict.keys():
            if possible_letter_and_length(teg, word,
                                          wrong_teg,
                                          letter_dict):
                continue
            test = levenshtein(wrong_teg, teg, False) == 1
            if test == 1:
                words = utils.make_list(big_dict.get(teg))
                correct += words
    minimum = float('inf')
    possible_mistakes = {}
    correct_word = ''
    correct_words = []
    for variant in correct:
        distance, f = levenshtein(variant, word, True)
        if distance == minimum:
            correct_words.append([variant, f])
            continue
        if distance < minimum:
            correct_words = [[variant, f]]
            minimum = distance
            correct_word = variant
            possible_mistakes[correct_word] = f
    if len(correct_words) > 2:
        return write_mistakes(word,
                              correct_words,
                              possible_mistakes.get(correct_word),
                              correct_word)
    return write_mistakes(word,
                          [],
                          possible_mistakes.get(correct_word),
                          correct_word)


def make_tag(word: str) -> str:
    spell_teg = ''
    position = 0
    length = len(word)
    while position != length:
        for number in [4, 3, 2, 1]:
            spell_teg, position, done = part_tag(spell_teg, word,
                                                 position, number, length)
            if done or position == length:
                break
    return spell_teg


def part_tag(spell_teg: str, word: str, position: int, number: int,
             length: int) -> (str, int, bool):
    teg = find_gram(word, position, number, length)
    if teg is None:
        return spell_teg, position, False
    else:
        spell_teg += teg
        position += number
        return spell_teg, position, True


def find_gram(word: str, position: int, number: int, length: int) -> str:
    if position <= length - number:
        word_part = word[position: position + number]
        if number != 1 and word_part == word[position] * number:
            return word[position]
        else:
            return NGRAMS.get(number).get(word_part)


def possible_letter_and_length(teg: str, word: str, wrong_teg: str,
                               letter_dict: dict) -> (int, bool):
    possible_letter = teg[0] in letter_dict[word[0]]
    possible_length = abs(len(wrong_teg) - len(teg)) <= 2
    return not (possible_letter and possible_length)


def levenshtein(string_a: str, string_b: str, flag: bool):
    long = []
    len_a = len(string_a)
    len_b = len(string_b)
    miss = ''
    for i in range(len_a + 1):
        long.append([i + j if i * j == 0 else 0 for j in range(len_b + 1)])
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if string_a[i - 1] == string_b[j - 1]:
                long[i][j] = long[i - 1][j - 1]
            else:
                long[i][j] = 1 + min(long[i - 1][j], long[i][j - 1],
                                     long[i - 1][j - 1])
                if flag and i - j == 0:
                    space = ', ' if miss else ' '
                    miss += space + str(i)
    if flag and abs(len_a - len_b) > 0:
        i = min(len_a, len_b) + 1
        j = max(len_a, len_b) + 1
        for o in range(i, j):
            space = ', ' if miss else ' '
            miss += space + str(o)
    if flag:
        return long[len(string_a)][len(string_b)], miss
    return long[len(string_a)][len(string_b)]


def write_mistakes(wrong: str, possible_variants: list, mistakes='',
                   correct='') -> str:
    if not mistakes:
        return ''
        # return f'{wrong} - Correct sentences\n'
    if possible_variants:
        return write_possible_mistakes(wrong,
                                       possible_variants)
    apostrophe = 's' if int(re.sub(r'[^0-9]', '', mistakes)) > 10 else ''
    return f'{wrong} - Mistake{apostrophe} in{mistakes} letter{apostrophe}, ' \
           f'maybe you mean -> {correct}\n'


def write_possible_mistakes(wrong: str, possible_variants: list) -> str:
    result = ''
    result += f'{wrong} - Some variants:\n'
    for word in possible_variants:
        if word[1] == '':
            word[1] = ' ' + str(len(word[0]))
        apostrophe = 's' if int(re.sub(r'[^0-9]', '', word[1])) > 10 else ''
        result += f'    Mistake{apostrophe} in{word[1]} letter{apostrophe}, ' \
                  f'maybe you mean -> {word[0]}\n'
    return result
