import unittest
from spellchecker.checker import checker, utils, dictionary_utils, writer, \
    tag_creator


class TestCreateDictionaryForMain(unittest.TestCase):
    def test_create_dictionary(self):
        self.correct_words = {'пурку': 'бурку',
                              'сакасаф': ['заказав', 'заказов'],
                              'кфас': 'квас'}
        self.dict = dictionary_utils.create_dictionary(r'test_dict.txt')
        self.assertEqual(self.dict, self.correct_words)


class TestChecker(unittest.TestCase):
    def test_spell_checker(self):
        correct = "превет - Mistake in 3 lettermaybe you mean -> привет\n"
        check = checker.spell_checker(dictionary_utils.create_dictionary(
            r"../dictionary.json"), "превет")
        self.assertEqual(correct, check)

    def test_possible_letter_and_length(self):
        poss_len = checker.find_possible_length('римскии', 'римский')
        self.assertEqual(poss_len, False)

    def test_length_optimization(self):
        poss_len = checker.find_possible_length('абвгде', 'абвг')
        self.assertEqual(poss_len, False)

    def test_letter_optimization(self):
        poss_len = checker.find_possible_length('обвгде', 'абв')
        self.assertEqual(poss_len, True)

    def test_levenshtein_true(self):
        levenshtein = checker.levenshtein('слово', 'неслово', True)
        true = (2, ' 1, 2, 3, 4, 6, 7')
        self.assertEqual(levenshtein, true)

    def test_levenshtein_false(self):
        levenshtein = checker.levenshtein('слово', 'неслово', False)
        self.assertEqual(levenshtein, 2)


class TestDictionaryUtils(unittest.TestCase):
    def test_create_dictionary(self):
        dict_test = dictionary_utils.create_dictionary(r"test_json")
        true = {"aa": ["a", "aaa"], "bb": ["b", "bbb"]}
        self.assertEqual(dict_test, true)


class TestTagCreator(unittest.TestCase):
    def test_make_teg(self):
        make_teg = tag_creator.make_full_tag('какое-тослово')
        true = 'какаитаслафа'
        self.assertEqual(make_teg, true)

    def test_part_teg(self):
        part_tag = tag_creator.make_part_tag('паукам', 'пауком', 1, 1, 6)
        true = ('паукама', 2, True)
        self.assertEqual(part_tag, true)

    def test_find_gram(self):
        find_gram = tag_creator.find_gram('пауком', 1, 1, 6)
        self.assertEqual(find_gram, "a")


class TestUtils(unittest.TestCase):
    def test_make_correct_line(self):
        test = 'праверка пр0шла бесуспешн1, зочеm вы ее ночинали?'
        correct_line = utils.make_correct_line(test)
        true = ['праверка', 'пршла', 'бесуспешн', 'зоче', 'вы', 'ее',
                'ночинали']
        self.assertEqual(correct_line, true)

    def test_make_list(self):
        test = 'праверка пр0шла бесуспешн1, зочеm вы ее ночинали?'
        make_test_list = utils.make_list(test)
        true = ['праверка', 'пршла', 'бесуспешн', 'зоче', 'вы', 'ее',
                'ночинали']
        self.assertEqual(make_test_list, true)


class TestWriter(unittest.TestCase):
    def test_write_mistake(self):
        string = writer.write_mistakes('абв', [['абвг', '4']], '4')
        print(string)
        true = 'абв - Mistake in 4 letter, maybe you mean -> абвг\n'
        self.assertEqual(string, true)

    def test_no_mistakes(self):
        string = writer.write_mistakes('абв', [], '')
        self.assertEqual(string, '')

    def test_write_possible_mistakes(self):
        raz = 'раздражена'
        string = writer.write_mistakes('расдраженно',
                                       ["раздраженно", "раздражена"], '')
        s = f'    Mistakes in 3, 10 - 11 letters, maybe you mean -> {raz}\n'
        true = 'расдраженно - Some variants:\n' + (
            '    Mistake in 3 letter, maybe you mean -> раздраженно\n') + s
        self.assertEqual(true, string)


if __name__ == '__main__':
    unittest.main()
