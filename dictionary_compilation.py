# -*- coding: utf8 -*-
import re
import os
import spell_checker
import Main

LIBRARY = r'library\\'
ENCODINGS = ['ansi', 'cp855', 'cp866', 'utf_16', 'utf_7',
             'koi8_r', 'iso8859_5', 'mac_cyrillic']


def file_reader(filename):
    words = set()
    for file in filename:
        try:
            words = give_words_from_file(file, words, 'utf8')
        except(UnicodeDecodeError, LookupError):
            words = give_words_from_file(file, words, encoding_define(file))
    return words


def give_words_from_file(file, words, encoding):
    with open(LIBRARY + file, encoding=encoding) as text:
        for line in text:
            words = find_words_in_line(line, words)
    return words


def find_words_in_line(line, words):
    reg = re.compile('[^а-яА-ЯёЁ\\- ]')
    line = reg.sub('', line)
    words_in_line = line.split()
    for word in words_in_line:
        if word[0] == '-':
            continue
        words.add(word.lower())
    return words


def encoding_define(file_name):
    for encoding in ENCODINGS:
        file = open(LIBRARY + file_name, encoding=encoding)
        try:
            file.read()
        except (UnicodeDecodeError, LookupError):
            file.close()
        else:
            file.close()
            return encoding


def create_dict(correct_test_words):
    dictionary = {}
    for word in correct_test_words:
        word = word.lower()
        teg = spell_checker.SpellChecker.make_teg(word)
        if teg == '':
            continue
        if teg not in dictionary.keys():
            dictionary[teg] = word
        else:
            dictionary[teg] += ', ' + word
    return dictionary


def write_in_file(dictionary):
    for key in dictionary.keys():
        key_word = dictionary.get(key)
        with open(Main.DICTIONARY, 'a', encoding='utf8') \
                as file_dict:
            file_dict.write(key + ': ' + key_word + '\n')


def main():
    files = os.listdir(LIBRARY)
    words = file_reader(files)
    dictionary = create_dict(words)
    write_in_file(dictionary)


if __name__ == '__main__':
    main()
