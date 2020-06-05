from spell_checker import spell_checker, utils, keys, GUI
from dictionary import create_dictionary_for_main as create_dict
import sys


if __name__ == '__main__':
    line = input('enter the key, for help enter "-h"\n')
    keys.parser_arguments(sys.argv[1:])

