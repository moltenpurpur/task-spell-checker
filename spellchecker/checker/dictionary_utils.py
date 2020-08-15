import json


def create_dictionary(dict_path: str) -> dict:
    with open(dict_path, encoding='utf8') as file_dictionary:
        big_dict = json.load(file_dictionary)
    return big_dict


def letter_dictionary(big_dict: dict) -> dict:
    dict_letters = {}
    for key in big_dict.keys():
        for word in big_dict.get(key):
            if dict_letters.get(word[0]):
                if key[0] not in dict_letters.get(word[0]):
                    tmp = dict_letters.get(word[0]) + key[0]
                    dict_letters.update({word[0]: tmp})
                else:
                    continue
            else:
                dict_letters[word[0]] = [key[0]]
    return dict_letters
