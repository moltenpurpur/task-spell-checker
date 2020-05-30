import re


def make_correct_line(line):
    return re.compile('[^à-ÿÀ-ß¸¨\\- ]').sub('', line).split()


def make_list(word_string):
    word_list = str(word_string)
    return re.compile('[^à-ÿ¸\\- ]').sub('', word_list).split()
