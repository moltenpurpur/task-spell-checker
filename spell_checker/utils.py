import re


def make_correct_line(line):
    return re.compile('[^�-��-߸�\\- ]').sub('', line).split()


def make_list(word_string):
    word_list = str(word_string)
    return re.compile('[^�-��\\- ]').sub('', word_list).split()
