import re
import os
from checker import spell_checker


def file_reader(filename: list, library: str) -> set:
    words = set()
    for file in filename:
        words = give_words_from_file(file, library)
    return words


def give_words_from_file(file: str, library: str) -> set:
    with open(library + file, encoding="utf-8") as text:
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


def write_in_file(dictionary: dict, dict_path):
    for key in dictionary.keys():
        key_word = dictionary.get(key)
        with open(dict_path, 'w', encoding='utf8') as file_dict:
            file_dict.write(key + ': ' + key_word + '\n')


def main_dict(library: str, dict_path: str):
    files = os.listdir(library)
    words = file_reader(files, library)
    dictionary = create_dict(words)
    write_in_file(dictionary, dict_path)

