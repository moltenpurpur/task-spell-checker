from spell_checker import spell_checker, utils
from dictionary import create_dictionary_for_main as create_dict


if __name__ == '__main__':
    line = input('enter words or sentences:')
    result_string = ''
    line = utils.make_correct_line(line)
    dictionary = create_dict.create_dictionary()
    letter_dict = create_dict.letter_dictionary(dictionary)
    for word in line:
        result_string += spell_checker.spell_checker(
            dictionary,
            letter_dict,
            word)
    print(result_string)
