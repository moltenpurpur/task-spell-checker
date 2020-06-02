import re


def make_correct_line(line):
    return re.sub(r'[^а-яА-ЯёЁ\- ]', '', line).split()


def make_list(word_string):
    word_list = str(word_string)
    return re.sub(r'[^а-яё\- ]', '', word_list).split()
