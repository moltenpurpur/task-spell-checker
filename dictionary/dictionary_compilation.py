import re
import os
from spell_checker import spell_checker
from dictionary import create_dictionary_for_main as cr_dict

LIBRARY = r'library\\'


def file_reader(filename: list) -> set:
    words = set()
    for file in filename:
        words = give_words_from_file(file)
    return words


def give_words_from_file(file: str) -> set:
    with open(LIBRARY + file, encoding="utf-8") as text:
        for line in text:
            words = find_words_in_line(line, words)
    return words


def find_words_in_line(line: str, words: set) -> set:
    reg = re.compile('[^а-яА-ЯёЁ\\- ]')
    line = reg.sub('', line)
    words_in_line = line.split()
    for word in words_in_line:
        if word[0] == '-':
            continue
        words.add(word.lower())
    return words


def create_dict(correct_test_words: set) -> dict:
    dictionary = {}
    for word in correct_test_words:
        word = word.lower()
        teg = spell_checker.make_tag(word)
        if teg == '':
            continue
        if teg not in dictionary.keys():
            dictionary[teg] = word
        else:
            dictionary[teg] += ', ' + word
    return dictionary


def write_in_file(dictionary: dict):
    for key in dictionary.keys():
        key_word = dictionary.get(key)
        with open(cr_dict.DICTIONARY, 'w', encoding='utf8') as file_dict:
            file_dict.write(key + ': ' + key_word + '\n')


def main_dict():
    files = os.listdir(LIBRARY)
    words = file_reader(files)
    dictionary = create_dict(words)
    write_in_file(dictionary)

