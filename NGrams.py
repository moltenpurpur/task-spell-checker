# -*- coding: utf8 -*-
ALPH = {
    'а': 'а', 'б': 'п', 'в': 'ф', 'г': 'к', 'д': 'т',
    'е': 'и', 'ё': 'а', 'ж': 'ш', 'з': 'с', 'и': 'и',
    'й': 'и', 'к': 'к', 'л': 'л', 'м': 'м', 'н': 'н',
    'о': 'а', 'п': 'п', 'р': 'р', 'с': 'с', 'т': 'т',
    'у': 'у', 'ф': 'ф', 'х': 'х', 'ц': 'ш', 'ч': 'ш',
    'ш': 'ш', 'щ': 'ш', 'ъ': '', 'ы': 'и', 'ь': '',
    'э': 'и', 'ю': 'у', 'я': 'а', '-': ''
}
BIGRAMS = {
    'cc': 'c', 'тс': 'ц', 'дц': 'ц', 'хг': 'г', 'сч': 'ш',
    'зч': 'ш', 'жч': 'ш', 'сш': 'ш', 'сщ': 'ш', 'тч': 'ш'
}
TRIGRAMS = {
    'стн': 'сн', 'ндш': 'нш', 'стл': 'сл', 'здн': 'зн',
    'здц': 'сц', 'лнц': 'нц', 'ндц': 'нц', 'нтг': 'нг',
    'рдц': 'рц', 'рдч': 'рч', 'стг': 'сг'
}
FOURGRAMS = {
    'вств': 'ств'
}