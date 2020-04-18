# -*- coding: utf8 -*-
import re
import NGrams
import Main

NGRAMS = {
    1: NGrams.ALPH, 2: NGrams.BIGRAMS, 3: NGrams.TRIGRAMS, 4: NGrams.FOURGRAMS
}


class SpellChecker:
    @staticmethod
    def spell_checker(big_dict, letter_dict, word):
        correct = []
        word = word.lower()
        wrong_teg = SpellChecker.make_teg(word)
        if big_dict.get(wrong_teg):
            words = Main.Main.make_list(big_dict.get(wrong_teg))
            correct += words
        else:
            for teg in big_dict.keys():
                if SpellChecker.possible_letter_and_length(teg, word,
                                                           wrong_teg,
                                                           letter_dict):
                    continue
                test = SpellChecker.levenshtein(wrong_teg, teg, False) == 1
                if test == 1:
                    words = Main.Main.make_list(big_dict.get(teg))
                    correct += words
        minimum = float('inf')
        possible_mistakes = {}
        correct_word = ''
        correct_words = []
        for variant in correct:
            distance, f = SpellChecker.levenshtein(variant, word, True)
            if distance == minimum:
                correct_words.append([variant, f])
                continue
            if distance < minimum:
                correct_words = [[variant, f]]
                minimum = distance
                correct_word = variant
                possible_mistakes[correct_word] = f
        if len(correct_words) > 2:
            return SpellChecker.write_mistakes(word, possible_mistakes.get(
                correct_word),
                                               correct_word, correct_words)
        return SpellChecker.write_mistakes(word,
                                           possible_mistakes.get(correct_word),
                                           correct_word, None)

    @staticmethod
    def make_teg(word):
        spell_teg = ''
        i = 0
        length = len(word)
        while i != length:
            for number in [4, 3, 2, 1]:
                spell_teg, i, done = SpellChecker.part_teg(spell_teg, word,
                                                           i, number, length)
                if done or i == length:
                    break
        return spell_teg

    @staticmethod
    def part_teg(spell_teg, word, i, number, length):
        teg = SpellChecker.find_gram(word, i, number, length)
        if teg is None:
            return spell_teg, i, False
        else:
            spell_teg += teg
            i += number
            return spell_teg, i, True

    @staticmethod
    def find_gram(word, index, number, length):
        if index <= length - number:
            word_part = word[index: index + number]
            if number != 1 and word_part == word[index] * number:
                return word[index]
            else:
                return NGRAMS.get(number).get(word_part)

    @staticmethod
    def possible_letter_and_length(teg, word, wrong_teg, letter_dict):
        possible_letter = teg[0] in letter_dict[word[0]]
        possible_length = abs(len(wrong_teg) - len(teg)) <= 2
        return not (possible_letter and possible_length)

    @staticmethod
    def levenshtein(a, b, flag):
        f = []
        len_a = len(a)
        len_b = len(b)
        miss = ''
        for i in range(len_a + 1):
            f.append([i + j if i * j == 0 else 0 for j in range(len_b + 1)])
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if a[i - 1] == b[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1],
                                      f[i - 1][j - 1])
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
            return f[len(a)][len(b)], miss
        return f[len(a)][len(b)]

    @staticmethod
    def write_mistakes(wrong, mistakes, correct, possible_variants):
        if not mistakes:
            return f'{wrong} - Correct sentences\n'
        if possible_variants:
            return SpellChecker.write_possible_mistakes(wrong,
                                                        possible_variants)
        s = 's' if int(re.compile('[^0-9]').sub('', mistakes)) > 10 else ''
        return f'{wrong} - Mistake{s} in{mistakes} letter{s}, ' \
               f'maybe you mean -> {correct}\n'

    @staticmethod
    def write_possible_mistakes(wrong, possible_variants):
        string = ''
        string += f'{wrong} - Some variants:\n'
        for word in possible_variants:
            if word[1] == '':
                word[1] = ' ' + str(len(word[0]))
            s = 's' if int(re.compile('[^0-9]').sub('', word[1])) > 10 else ''
            string += f'    Mistake{s} in{word[1]} letter{s}, ' \
                      f'maybe you mean -> {word[0]}\n'
        return string
