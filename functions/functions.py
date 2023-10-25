"=============Функции==========="
# функция - именованный блок кода, который может принимать аргументы и возвращать результат

# def func(x:int, y:int) -> None: # параметры
#     """
#     this function return x + y
#     """
#     print(x)
#     print(y)
#     return x + y # возвращаю результат  
# func(5, 4) # аргументы

# def mul(x:int,y:int,z:int)-> int:
#     """
#     multiply x,y,z
#     """
#     return x*y*z
# result = mul(2,3,4)
# print(result)

# наисать функцию my_len которая принимает строку и возвращает длину этой строки

def my_len(string:str):
    print(string)
    return print(len(string))
my_len('hello')

def my_len(string:str):
    counter = 0
    for i in string:
        counter+=1
    return counter
print(my_len('hello'))

# DRY - don't repeat yourself

"================Аргументы и параметры============="
# параметры - переменные внутри функции, значения которые мы задаем при вызове функции (рецепт пиццы)
# аргументы - значения, которые мы передаем при вызове функции (ингридиенты пиццы)

"===============Виды параметров============"
# 1.обязательные
# 2.не обязательные
# 2.1 с дефолтом (по умолчанию)
# 2.2. args
# 2.3 kwargs

# def func(a, b=3):
#     return a + b
# print(func(1)) # 4
# def func(a, b=3):
#     return a + b
# print(func(1,2)) # 3

def func(a, b=3, *args):
    print(args)
    return a + b
print(func(a=4,b=5))

"=================Виды аргументов==========="
print("=================Виды аргументов===========")
# 1. - позиционные
# 2. - именованные

def func(a, b=5, *hh):
    return a*b
print(func(1,2,3))
func(a=5,b=435)
number1 = 6
number2 = 7
func(number1, number2) # 42
func(b=5, a=435)
# func(a=5, 4) # SyntaxError:
func(4, b=5)

# надо написать функцию которая принимает строку

def reverse(string:str)->str:
    return string[::-1]
reverse('hello') # olleh

def func():
    print(5)
    return func
func()()

def translate(string:str):
    eng = "qwerty"
    ru = "йцукен"
    if string[0] in eng:
        dict_ = ''.maketrans(eng, ru)
    else:
        dict_ = ''.maketrans(ru, eng)
    return string.maketrans(dict_)
print(translate('hello'))

# надо написать функцию 

def is_palindrome(string:str)->bool:
    if string[::-1].lower() == string.lower():
        print(True)
    else:
        print(False)
    return
is_palindrome('dad')

# рекурсия -  ДЗ

"=================Анонимная функция================="
# lambda - анонимная функция, которая записывается в одну строчку
print("=================Анонимная функция=================")
func = lambda x:x**10
print(func(2)) # 1024

# def plus(a1, a2):
#     return a1+a2
# def minus(a1, a2):
#     return a1-a2
# def mul(a1, a2):
#     return a1*a2
# def div(a1, a2):
#     return a1//a2
def main():
    try:
        num1 = int(input('num1: '))
        num2 = int(input('num2: '))
        operation = input('opeation choise: + | - | * | /')
        calc = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x//y,
        }
        func = (calc.get(operation, 'такой операции нет'))
        print(func(num1, num2))
    except ValueError:
        print('Введите число!!!')
    except KeyError:
        print('Неизвестный оператор')
    except ZeroDivisionError:
        print('Дурак на 0 делить?')
    finally:
        print('bb all')

while True:
    main()
    answer = input('завершить? (y/n)')
    if answer.lower() == 'y':
        break



def func(a,b, *args, kwargs):
    pass
func(3,4,5,6)