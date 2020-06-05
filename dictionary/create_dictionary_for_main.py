from spell_checker import utils

DICTIONARY = r'dictionary.txt'


def create_dictionary() -> dict:
    big_dict = {}
    with open(DICTIONARY, encoding='utf8') as file_dictionary:
        for line in file_dictionary:
            spell_teg = line.strip().split(':')[0]
            words = line.strip().split(':')[1].lstrip()
            big_dict[spell_teg] = utils.make_list(words)
    return big_dict


def letter_dictionary(big_dict: dict) -> dict:
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
