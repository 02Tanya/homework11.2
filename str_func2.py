def get_lowercase_phrase():
    '''Переводит фразу в верхний регистр'''
    phrase = input('Введите фразу или предложение: ')
    return phrase.lower()


def get_first_letter_up():
    '''Повышает регистр первой буквы каждого слова'''
    phrase = input('Введите фразу или предложение: ')
    return phrase.title()
