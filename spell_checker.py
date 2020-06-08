import sys
import argparse
from dictionary import create_dictionary_for_main as create_dict
from dictionary import dictionary_compilation
from checker import checker, utils
import gui


def parser_arguments():
    library_default = r'library\\'
    dictionary_default = r'dictionary.txt'
    input_text_file = r'input_text_file.txt'
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_append_compile = subparsers.add_parser('compile',
                                                  help='select .txt files to '
                                                       'compile the dictionary'
                                                       '(Default: library//, '
                                                       'dictionary.txt)',
                                                  )
    parser_append_compile.set_defaults(function=compile_dictionary)

    parser_append_compile.add_argument('--library',
                                       default=library_default,
                                       type=str,
                                       help='path to text or text folder'
                                            '(Default: library//)',
                                       dest='library')
    parser_append_compile.add_argument('--dictionary',
                                       default=dictionary_default,
                                       type=str,
                                       help='dictionary output file '
                                            '(Default: dictionary.txt)',
                                       dest='dictionary')

    parser_append_check = subparsers.add_parser('check',
                                                help='checking text from file')
    parser_append_check.set_defaults(function=check_file)

    parser_append_check.add_argument('--dictionary ',
                                     default=dictionary_default,
                                     type=str,
                                     help='path to dictionary'
                                          '(Default: dictionary.txt)',
                                     dest='dictionary')
    parser_append_check.add_argument('--input_file',
                                     default=input_text_file,
                                     help='text to check'
                                          '(Default: input_text_file.txt)',
                                     dest='file')

    parser_append_gui = subparsers.add_parser('gui',
                                              help='call gui')
    parser_append_gui.set_defaults(function=call_gui)

    args = parser.parse_args()
    args.function(args)


def call_gui(args):
    gui.main_gui()


def compile_dictionary(args):
    dictionary_compilation.main_dict(args.library, args.dictionary)


def check_file(args):
    with open(args.file) as file:
        line = file.readline()

        while line:
            result_string = ''
            line = utils.make_correct_line(line)
            dictionary = create_dict.create_dictionary(args.dictionary)
            letter_dict = create_dict.letter_dictionary(dictionary)
            for word in line:
                result_string += checker.spell_checker(
                    dictionary,
                    letter_dict,
                    word)
            line = file.readline()
            print(result_string)


if __name__ == '__main__':
    parser_arguments()
