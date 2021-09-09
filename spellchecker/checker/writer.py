import re


def write_mistakes(wrong: str, possible_variants: list, mistakes='') -> str:
    result = ''
    if not mistakes:
        return ''
    result += f'{wrong} - '
    # indent = ''
    if len(possible_variants) > 1:
        # indent = '    '
        result += 'Some variants:\n'
    for word in possible_variants:
        if word[1] == '':
            word[1] = ' ' + str(len(word[0]))
        result += f'Word:{word[1]}\n{word[0]}\n\n'
        # apostrophe = 's' if int(re.sub(r'[^0-9]', '', word[1])) > 10 else ''
        # result += f'{indent}Mistake{apostrophe} in{word[1]} ' \
        #           f'letter{apostrophe}maybe you mean -> {word[0]}\n'
    return result
