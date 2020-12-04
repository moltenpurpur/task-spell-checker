import os
import re
import json
from collections import defaultdict
from spellchecker.checker import tag_creator, n_grams


class DictionaryCompiler:
    NOT_WORD_REGEX = re.compile(r'[^а-яА-ЯёЁ\- ]+')

    def __init__(self, *library_paths, encoding: str = 'utf-8'):
        self.library_paths = library_paths
        self.file_queue = [*self.library_paths]
        self.encoding = encoding
        self.library = list()

    def collect_texts(self):
        library = []
        while self.file_queue:
            path = self.file_queue.pop(0)
            path = os.path.abspath(path)
            if os.path.isdir(path):
                for sub_path in os.listdir(path):
                    self.file_queue.append(path + '\\' + sub_path)
            elif path.endswith('.txt'):
                library.append(path)
        return library

    def extract_words_from_file(self, path):
        words = set()
        with open(path, encoding=self.encoding) as f:
            try:
                for line in f:
                    for word in self.NOT_WORD_REGEX.sub('', line).split():
                        words.add(word.lower())
            except Exception:
                print(f'something is wrong with your text: {f.name}, '
                      f'the program cannot read it')
        return words

    @staticmethod
    def compile(words: set) -> dict:
        tag_map = defaultdict()
        for letter in n_grams.ALPH:
            d = defaultdict(list)
            for word in words:
                tag = tag_creator.make_full_tag(word)
                if tag != '' and tag[0] == letter:
                    d[tag].append(word)

            tag_map[letter] = d
        return tag_map

    @staticmethod
    def write_tag_map_in_file(tag_map, file='dictionary.json'):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(tag_map, f, ensure_ascii=False)

    @classmethod
    def build_tag_map(cls, *library_paths, encoding: str = 'utf-8',
                      dictionary_paths):
        compiler = cls(*library_paths, encoding=encoding)
        words = set()
        for path in compiler.collect_texts():
            words |= compiler.extract_words_from_file(path)
        tag_map = cls.compile(words)
        return DictionaryCompiler.write_tag_map_in_file(tag_map,
                                                        dictionary_paths)
