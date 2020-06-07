import argparse
from dictionary import create_dictionary_for_main as create_dict
from dictionary import dictionary_compilation
from spell_checker import GUI, spell_checker, utils


def parser_arguments(args):
    library_default = r'library\\'
    parser = argparse.ArgumentParser()

    parser.add_argument('-dc', '--dictionary_compilation',
                        default=library_default,
                        type=str,
                        help='select .txt files to compile the dictionary '
                             '(Default: library//)')
    parser.add_argument('-g', '--GUI',
                        help='invokes a graphical interface',
                        action='store_true')
    parser.add_argument('-c', '--console',
                        help='starts the program from the console',
                        action='store_true')

    args = parser.parse_args(args)

    if args.dictionary_compilation != library_default:
        change_dictionary()
    elif args.GUI:
        GUI.main_gui()
    elif args.console:
        main_console()


def main_console(library=r'library//', dict_path=r'dictionary.txt'):
    line = input('enter words or sentences: ')
    result_string = ''
    if library != r'library//' and dict_path != r'dictionary.txt':
        dictionary_compilation.main_dict(library, dict_path)
    line = utils.make_correct_line(line)
    dictionary = create_dict.create_dictionary(dict_path)
    letter_dict = create_dict.letter_dictionary(dictionary)
    for word in line:
        result_string += spell_checker.spell_checker(
            dictionary,
            letter_dict,
            word)
    print(result_string)


def change_dictionary():
    library = input('input path library: ')
    dict_path = input('enter the path to write the dictionary: ')
    main_console(library, dict_path)

