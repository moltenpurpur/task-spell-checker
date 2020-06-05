##################
#  does not work #
##################
import argparse
from dictionary.create_dictionary_for_main import DICTIONARY
from dictionary.dictionary_compilation import LIBRARY
from dictionary import create_dictionary_for_main as create_dict
from spell_checker import GUI, spell_checker, utils


def parser_arguments(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('-dc', '--dictionary_compilation',
                        default=LIBRARY,
                        type=str,
                        help='select .txt files to compile the dictionary '
                             '(Default: library//)')
    parser.add_argument('-de', '--dictionary_export',
                        default=DICTIONARY,
                        type=str,
                        help='select a .txt file to transfer the dictionary '
                             '(Default: dictionary.txt)')
    parser.add_argument('-g', '--GUI',
                        help='invokes a graphical interface',
                        action='store_true')
    parser.add_argument('-c', '--console',
                        help='starts the program from the console')

    args = parser.parse_args(args)

    if args.dictionary_compilation != LIBRARY:
        print('dict_comp')
    elif args.dictionary_export != DICTIONARY:
        print('dict_export')
    elif args.GUI:
        GUI.main_gui()
    else:
        main_console()


def main_console():
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
