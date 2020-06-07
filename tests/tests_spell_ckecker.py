import unittest
from checker import spell_checker, utils
from dictionary import create_dictionary_for_main as cr_dict
from dictionary import dictionary_compilation as dict_comp


class TestMain(unittest.TestCase):
    def test_make_correct_line(self):
        test = 'праверка пр0шла бесуспешн1, зочеm вы ее ночинали?'
        self.correct_line = utils.make_correct_line(test)
        self.true = ['праверка', 'пршла', 'бесуспешн', 'зоче', 'вы', 'ее',
                     'ночинали']
        self.assertEqual(self.correct_line, self.true)

    def test_create_dictionary(self):
        pass

    def test_make_list(self):
        test = 'праверка пр0шла бесуспешн1, зочеm вы ее ночинали?'
        self.list = utils.make_list(test)
        self.true = ['праверка', 'пршла', 'бесуспешн', 'зоче', 'вы', 'ее',
                     'ночинали']
        self.assertEqual(self.list, self.true)


class TestSpellChecker(unittest.TestCase):
    def test_spell_checker(self):
        test_dict = {'апф': ['обв'], 'а': ['о'], 'ап': ['об']}
        test_litter_d = {'о': ['а'], 'a': ['a']}
        test_word = 'абв'
        self.spell_checker = spell_checker.spell_checker(
            test_dict, test_litter_d, test_word)
        self.true = 'абв - Mistake in 1 letter, maybe you mean -> обв\n'
        self.assertEqual(self.spell_checker, self.true)

    def test_make_teg(self):
        test = 'какое-тослово'
        self.make_teg = spell_checker.make_tag(test)
        self.true = 'какаитаслафа'
        self.assertEqual(self.make_teg, self.true)

    def test_part_teg(self):
        test_spell_teg = 'паукам'
        test_word = 'пауком'
        test_i = 1
        test_number = 1
        test_length = 6
        self.part_tag = spell_checker.part_tag(test_spell_teg,
                                               test_word, test_i,
                                               test_number,
                                               test_length)
        self.true = ('паукама', 2, True)
        self.assertEqual(self.part_tag, self.true)

    def test_find_gram(self):
        test_word = 'пауком'
        test_i = 1
        test_number = 1
        test_length = 6
        self.find_gram = spell_checker.find_gram(test_word,
                                                 test_i,
                                                 test_number,
                                                 test_length)
        self.true = 'а'
        self.assertEqual(self.find_gram, self.true)

    def test_possible_letter_and_length(self):
        self.poss_l = spell_checker.possible_letter_and_length(
            'римскии', 'римский', 'римскии',
            {'р': ['р', 'с']})
        self.assertEqual(self.poss_l, False)

    def test_length_optimization(self):
        self.poss_l = spell_checker.possible_letter_and_length(
            'абвгде', 'абвг', 'абв',
            {'а': ['а']})
        self.assertEqual(self.poss_l, True)

    def test_letter_optimization(self):
        self.poss_l = spell_checker.possible_letter_and_length(
            'обвгде', 'абвг', 'абв',
            {'а': ['а']})
        self.assertEqual(self.poss_l, True)

    def test_levenshtein_true(self):
        test_a = 'слово'
        test_b = 'неслово'
        test_flag = True
        self.levenshtein = spell_checker.levenshtein(test_a,
                                                     test_b,
                                                     test_flag)
        self.true = (2, ' 1, 2, 3, 4, 6, 7')
        self.assertEqual(self.levenshtein, self.true)

    def test_levenshtein_false(self):
        test_a = 'слово'
        test_b = 'неслово'
        test_flag = False
        self.levenshtein = spell_checker.levenshtein(test_a,
                                                     test_b,
                                                     test_flag)
        self.true = 2
        self.assertEqual(self.levenshtein, self.true)

    def test_write_mistake(self):
        self.string = spell_checker.write_mistakes('абв', [], '4',
                                                   'абвг')
        self.true = 'абв - Mistake in 4 letter, maybe you mean -> абвг\n'
        self.assertEqual(self.string, self.true)

    def test_no_mistakes(self):
        self.string = spell_checker.write_mistakes('абв', [], '', '')
        self.true = ''
        self.assertEqual(self.string, self.true)

    def test_write_possible_mistakes(self):
        raz = 'раздражена'
        s = f'    Mistakes in 3, 10 - 11 letters, maybe you mean -> {raz}\n'
        self.true = 'расдраженно - Some variants:\n' + (
            '    Mistake in 3 letter, maybe you mean -> раздраженно\n') + s


class TestDictionaryCompilation(unittest.TestCase):
    def test_find_words_in_line(self):
        self.words = set()
        self.line = 'Зачем ты начал эту проверку?'
        self.word_find = dict_comp.find_words_in_line(self.line, self.words)
        self.right = {'зачем', 'ты', 'начал', 'эту', 'проверку'}
        self.assertEqual(self.word_find, self.right)

    def test_find_words_in_line_english(self):
        self.words = set()
        self.line = 'Зачем you начал this проверку?'
        self.word_find = dict_comp.find_words_in_line(self.line, self.words)
        self.right = {'зачем', 'начал', 'проверку'}
        self.assertEqual(self.word_find, self.right)


class TestCreateDictionaryForMain(unittest.TestCase):
    def test_create_dictionary(self):
        self.correct_words = {'пурку': 'бурку',
                              'сакасаф': ['заказав', 'заказов'],
                              'кфас': 'квас'}
        self.dict = cr_dict.create_dictionary(r'test_dict.txt')
        self.assertEqual(self.dict, self.correct_words)

    def test_letter_dictionary(self):
        test = {'проверка': 'проверка'}
        self.letter_dictionary = cr_dict.letter_dictionary(test)
        self.true = {'п': ['п'], 'р': ['п'], 'о': ['п'], 'в': ['п'],
                     'е': ['п'], 'к': ['п'], 'а': ['п']}
        self.assertEqual(self.letter_dictionary, self.true)


if __name__ == '__main__':
    unittest.main()
