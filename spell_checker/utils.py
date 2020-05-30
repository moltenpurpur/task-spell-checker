import re


def make_correct_line(line):
    return re.compile('[^а-яА-ЯёЁ\\- ]').sub('', line).split()


def make_list(word_string):
    word_list = str(word_string)
    return re.compile('[^а-яё\\- ]').sub('', word_list).split()
