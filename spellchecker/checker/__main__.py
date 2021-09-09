import argparse

from spellchecker.checker import checker, utils
from spellchecker.dictionary import dictionary_utils, dictionary_compilation
from spellchecker import gui


def parser_arguments():
    library_default = r'library//'
    dictionary_default = r'dictionary.json'
    input_text_file = r'../../input_text_file.txt'
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_append_compile = subparsers.add_parser('compile',
                                                  help='select .txt files to '
                                                       'compile the dictionary'
                                                       '(Default: library//, '
                                                       'dictionary.json)',
                                                  )
    parser_append_compile.set_defaults(function=compile_dictionary)

    parser_append_compile.add_argument(
        '--library',
        default=library_default,
        type=str,
        help='path to text or text folder(Default: library//)',
        dest='library')
    parser_append_compile.add_argument(
        '--encoding',
        default='utf-8',
        type=str,
        help='encoding (Default: utf-8)',
        dest='encoding')
    parser_append_compile.add_argument(
        '--dictionary',
        default=dictionary_default,
        type=str,
        help='dictionary output file (Default: dictionary.json)',
        dest='dictionary')

    parser_append_check = subparsers.add_parser('check',
                                                help='checking text from file')
    parser_append_check.set_defaults(function=spell_check)

    parser_append_check.add_argument(
        '--dictionary ',
        default=dictionary_default,
        type=str,
        help='path to dictionary(Default: dictionary.json)',
        dest='dictionary')
    parser_append_check.add_argument(
        '--input_file',
        default=input_text_file,
        help='text to check(Default: input_text_file.txt)',
        dest='file')

    parser_append_gui = subparsers.add_parser('gui',
                                              help='call gui')
    parser_append_gui.set_defaults(function=call_gui)

    args = parser.parse_args()
    args.function(args)


def call_gui(args):
    gui.main_gui()


def compile_dictionary(args):
    dictionary_compilation.DictionaryCompiler.build_tag_map(
        args.library, encoding=args.encoding,
        dictionary_paths=args.dictionary)


def spell_check(args):
    with open(args.file) as file:
        for line in file:
            result_string = []
            line = utils.make_correct_line(line)
            dictionary = dictionary_utils.create_dictionary(args.dictionary)
            for word in line:
                result_string.append(checker.spell_checker(dictionary, word))
            print(result_string)


if __name__ == '__main__':
    parser_arguments()
