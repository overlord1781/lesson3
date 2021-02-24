# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
from typing import Counter


students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
a = Counter(student['first_name'] for student in students).most_common()
for item in a:
	print(f'{item[0]}:{item[1]}')
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

a = Counter(student['first_name'] for student in students).most_common()[0]

print(f'Самое частое имя среди учеников: {a[0]} повторяется {a[1]} раз')
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
number_class = 1
for students_in_class in school_students:
	s = Counter(student['first_name'] for student in students_in_class).most_common()[0]
	print(f'Самое частое имя в классе {number_class} {s[0]} {s[1]}')
	number_class+=1 #!!!!!!! Решение с добавлением цифры класса текущей итеррации кажется мне лютейшим костылём но к моему стыду я не смог пока придумать лучше

# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print('\n')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}]}, #Проверка на болше учеников
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  {'class': '4ы', 'students': [{'first_name': 'Миша'}, {'first_name': 'Миша'}]} #При подстановки одинаковых имен программа работает некоректно из-за Counter
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_number in school:
    c = Counter(student['first_name'] for student in class_number.get('students'))
    i = class_number.get('class')
    boys = 0
    girls = 0
    for student in c:
        if is_male.get(student)==True:
            boys += c.get(student) #Мы пребавляем не +1 а + ученик, в случае совпадения, чтобы при одинаковых именнах программа не пропускала значения 
        else: 
            girls += c.get(student)

    print(f'В классе {i} {girls} девочки и {boys} мальчика')

# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


print('\n')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
  {'class': '4c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
  {'class': '4ы', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
  {'class': '9c', 'students': [{'first_name': 'Маша'}, {'first_name': 'Маша'}, {'first_name': 'Маша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
boys_2 = 0
girls_2 = 0
for class_number in school:# Здесь я перебираю словари в начальном спсике {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]}
    c = list(student['first_name'] for student in class_number.get('students')) #Из каждого словаря я генирую новый список оставляя в нем имена
    print(c)
    i = class_number.get('class') # Задаю в цикле текущий класс, который обрабатывается в первом цикле
    boys = 0
    girls = 0
    for student in c: # Перебираем элементы полученного списка 
        if student in is_male and is_male.get(student)==True:
            boys += 1
        else:
            girls +=1
        if boys>= boys_2:
            boys_2 = boys
            y = class_number.get('class')
        if girls >= girls_2:
            girls_2 = girls
            x = class_number.get('class')
    print(boys_2)
    print(boys)
print(y)
print(f'Больше всего мальчиков в классе {y}')
print(f'Больше всего девочек в классе {x}')

# Пример вывода:    
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a