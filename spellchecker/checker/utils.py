import re


def make_correct_line(line: str) -> list:
    return re.sub(r'[^а-яА-ЯёЁ\- \n]', '', line).split()


def make_list(word_string: str) -> list:
    word_list = str(word_string)
    return re.sub(r'[^а-яё\- ]', '', word_list).split()

