from collections import Counter

# text = input('Enter text: ')
text = 'Ajhoj sdfsdf fgfhgd'
letter_dict = Counter()
word_dict = Counter()

for i in text:
    if i not in [' ', '.', ',', ':', ';', '...', ';']:
        letter_dict.update(i)

text_list = text.split()
for i in text_list:
    word_dict.update([i])

print(word_dict)
print(letter_dict)