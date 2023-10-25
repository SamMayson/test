"=========Строки=========="
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), 
# заключенного в одинарные или двойные кавычки

string = 'Hello World'
string1 = "Hello World"
string2 = "Don't Hello World" # внутри двойных ковычек, одиночные кавычки и на оборот, воспринимаются как просто символ в тексте
string3 = 'текст - "text"'

'''  "text" 'text'     '''
"""  "text" 'text'     """

print('qq' + '2') # qq2
print('qq' * 2) # qqqq
string4 = 'Hello'
string5 = 'World'
print(string4+' '+string5) # Hello World

# Конкатенация - склеивание строк

"============Экранизация строк============"
'\n' # перенос на новую строку
print('hello\nworld')
# hello
# world

'\t' # табуляция
print('hello\tworld') # hello   world

print('Dont\'t')
print("Don\"t")
print("hello \\nero")
# hello \nero

'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки
print('Hello\vworld\vby\vsam)')
# Hello
#      world
#           by
#             sam)

"============Форматирование строк==========="
title = 'plov'
price = 200

print(f'Название:{title}\nЦена:{price}')
# Название:plov
# Цена:200

# -
tovar = str(input('Введите название товара: '))
print(f'{tovar} был вкусный')
# Введите название товара: Самса
# Самса был вкусный

format2 = 'Название: {}\nЦена: {}'
print(format2.format(title, price))

"=======================Методы строк=============="
# методы - функции, которая относится к определенному классу (типу данных), к ним мы обращаемся через точку

# print(dir(str))

'HELLO'.lower() # hello
'hello'.upper() # HELLO

'HEllO'.swapcase() # heLLo
'hello world'.capitalize() # Hello world
'hello world'.title() # Hello World
'hello world'.capitalize().swapcase # hELLO WORLD

'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello world'.count('makers') # 1

'hello world'.startswith('hello') # True
'hello world'.startswith('Hello') # False
'hello world'.endswith('world') # True
'hello world'.endswith('wordl') # False

'hello world'.islower() # True
'Hello World'.islower() # False
'HELLO WORLD'.isupper() # True
'hello world'.isupper() # False
'1234'.isdigit() # True
'1234salam'.isdigit() # False
'hello !'.isalpha() # True
'hello !'.isalnum() # False
'1234 '.isalnum() # False
'h1'.isalnum() # True

'hello world'.split(' ') # ['hello', 'world']
'hello world'.split('o') # ['hell', 'w', ' rld]
'hello world'.split('makers') # ['hello world']

' '.join(['hello',  'world']) # hello world
'1'.join(['hello',  'world']) # hello1world
'2'.join(['hello',  'world', 'RT']) # hello1world1RTх

string10 = '                                hello world           '
string10.strip() # hello world
string11 = '                                hello world           '
string11.lstrip() # "hello world                      "
string12 = '                                hello world           '
string12.rstrip() # "                      hello world"

string13 = '$$$SAM$$$$$'
string13.strip('$') # SAM

string14 = '&&&SUPER&&&&'
string14.replace('&', '') # SUPER
string14.replace('&', '', 2) # &SUPER&&&&

"=========================Идексы================="

# индекс - порядковый номер эдемента в последовательности (символ в строке) (индексация начинается с 0)

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#           ...-3 -2  -1
string = 'hello world'
string[2] # 'l'
string[0] # 'h'
string[6] # 'w'
string[10] # 'd'
string[-1] # 'd'

# срез - подстрока строки
print(string[0:5]) # hello
print(string[0:4]) # hell
print(string[6:10]) # worl
print(string[6:-1]) # world
print(string[6:11]) # world
print(string[:5]) # hello
print(string[:]) # hello world
print(string[:2] + string[-2:]) # he + ld | held

string[::2] # hlowrd
string[::-1] # dlrow olleh
string[::-2] # drwolh
string[::3] # hlwl

# question isnumeric|isdigid|isdecimal ?

immutable_string = 'hello'
immutable_string.upper()
# immutable_string = immutable_string.upper() # HELLO
# immutable_string = immutable_string[::-1] # OLLEH
print(immutable_string) # hello

string = 'world'
string[:-3] # wo
print(string) # world

a = list('Java:('.replace('J','P'))
a.pop(1)
a.pop(1)
print(''.join(a))
