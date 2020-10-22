import json


def create_dictionary(dict_path: str) -> dict:
    with open(dict_path, encoding='utf8') as file_dictionary:
        big_dict = json.load(file_dictionary)
    return big_dict
