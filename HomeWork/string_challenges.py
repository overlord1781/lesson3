# Вывести последнюю букву в слове
from typing import Collection


word = 'Архангельск'
print(word[-1])
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
item = 0
for lit in word.lower():
    if lit == 'а':
        item+=1
print(f'кол-во букв a в слове:{item}')
# ???

# Вывести количество букв "а" в слове
word = 'Архангельск'
item = word.lower().count('а')
print(f'кол-во букв a в слове:{item} с помощью коунт')
# ???



# Вывести количество гласных букв в слове

list_glasni = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'ё']

word = 'Архангельск'
clovo_glasni=0
for item in word.lower():
    if item in list_glasni:
        clovo_glasni+=1
print(f'Кол-во гласных в слове:{clovo_glasni}')
        
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
list_slov = sentence.split()
print(f"Кол-во слов в фразе:{len(list_slov)}")
# ???

print('\n')
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_slov = sentence.split()
for item in list_slov:
    print (item[0])
print('\n')
# ???


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
list_slov = sentence.split()
all_bukv = 0
all_slov = len(list_slov)
for item in list_slov:
    all_bukv += len(item)
print(f'средняя длина слова:{all_bukv/all_slov}')
# ???