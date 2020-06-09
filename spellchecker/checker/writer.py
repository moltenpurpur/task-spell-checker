import re


def write_mistakes(wrong: str, possible_variants: list, mistakes='',
                   correct='') -> str:
    if not mistakes:
        return ''
        # return f'{wrong} - Correct sentences\n'
    if possible_variants:
        return write_possible_mistakes(wrong,
                                       possible_variants)
    apostrophe = 's' if int(re.sub(r'[^0-9]', '', mistakes)) > 10 else ''
    return f'{wrong} - Mistake{apostrophe} in{mistakes} letter{apostrophe}, ' \
           f'maybe you mean -> {correct}\n'


def write_possible_mistakes(wrong: str, possible_variants: list) -> str:
    result = ''
    result += f'{wrong} - Some variants:\n'
    for word in possible_variants:
        if word[1] == '':
            word[1] = ' ' + str(len(word[0]))
        apostrophe = 's' if int(re.sub(r'[^0-9]', '', word[1])) > 10 else ''
        result += f'    Mistake{apostrophe} in{word[1]} letter{apostrophe}, ' \
                  f'maybe you mean -> {word[0]}\n'
    return result