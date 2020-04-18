# -*- coding: utf8 -*-
import re
import spell_checker

DICTIONARY = r'dictionary.txt'


class Main:
    @staticmethod
    def make_correct_line(line):
        return re.compile('[^а-яА-ЯёЁ\\- ]').sub('', line).split()

    @staticmethod
    def create_dictionary():
        big_dict = {}
        with open(DICTIONARY, encoding='utf8') as file_dictionary:
            for line in file_dictionary:
                spell_teg = line.strip().split(':')[0]
                words = line.strip().split(':')[1].lstrip()
                big_dict[spell_teg] = Main.make_list(words)
        return big_dict

    @staticmethod
    def make_list(word_string):
        word_list = str(word_string)
        return re.compile('[^а-яё\\- ]').sub('', word_list).split()

    @staticmethod
    def letter_dictionary(big_dict):
        dict_letters = {}
        for key in big_dict.keys():
            for word in big_dict.get(key):
                if dict_letters.get(word[0]):
                    if key[0] not in dict_letters.get(word[0]):
                        tmp = dict_letters.get(word[0]) + [key[0]]
                        dict_letters.update({word[0]: tmp})
                    else:
                        continue
                else:
                    dict_letters[word[0]] = [key[0]]
        return dict_letters

    @staticmethod
    def main():
        print('enter words or sentences:')
        line = input()
        result_string = ''
        line = Main.make_correct_line(line)
        dictionary = Main.create_dictionary()
        letter_dict = Main.letter_dictionary(dictionary)
        for word in line:
            result_string += spell_checker.SpellChecker.spell_checker(
                dictionary,
                letter_dict,
                word)
        print(result_string)


if __name__ == '__main__':
    Main.main()
