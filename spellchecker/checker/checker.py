from spellchecker.checker import tag_creator, utils, writer


def spell_checker(big_dict: dict, letter_dict: dict, word: str):
    correct = []
    word = word.lower()
    wrong_teg = tag_creator.make_full_tag(word)
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
        return writer.write_mistakes(word,
                                     correct_words,
                                     possible_mistakes.get(correct_word),
                                     correct_word)
    return writer.write_mistakes(word,
                                 [],
                                 possible_mistakes.get(correct_word),
                                 correct_word)


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


