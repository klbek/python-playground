from collections import Counter

text = input('Enter text: ')


def key_value_print(counter):
    for key, value in counter.items():
        print(f'{key}: {value}')


def calc_letter(text):
    letter_dict = Counter()
    for i in text:
        if i not in [' ', '.', ',', ':', ';', '...', ';', '(', ')']:
            letter_dict.update(i.lower())
    return key_value_print(letter_dict)


def calc_word(text):
    word_dict = Counter()
    text_list = text.lower().split()
    for i in text_list:
        word_dict.update([i])
    return key_value_print(word_dict)

# calc_word(text)
# calc_letter(text)