"===================Области видимости============"
# LEGB - local enclosed global build-in

"===================Build-in=================="
# встроенное пространство имен - (print, input, max, min.....)
# print(dir(__builtins__))
"===================Global===================="
# это пространство имен в котором хранятся все глобальные переменные, которые мы обьявили внутри этого файла
# что бы посмотреть все глобальные переменные, можно использовать globals

def func():
    pass
print(dir(globals()))
b = 7
print(globals())
print(func())
n = 8

"==============Enclosed==========="
# замкнутое пространство имен - локальное пространство у которого есть внутренное локальное пространство

var = 'глобальная переменная'
print(var)
def func():
    var = 'замкнутая переменная'
    print(var)
    def inner_func():
        var = 'локальная переменная'
        print(var)
    inner_func()
func()
# global enclosed local

"================Local==========="
# локальное пространство имен - переменные, созданные внутри функции

a = 10
def func(a,b):
    print('GLOBAL', globals()) # {a:10, func:<link>}
    n = 8
    def inner_func(a,b):
        pass
    inner_func(6,7)
    print('LOCAL', locals()) # LOCAL {'a': 5, 'b': 7, 'n': 8, 'inner_func': <function func.<locals>.inner_func at 0x100bb81f0>}
func(5,7)

count = 0
def counter():
    global count
    count+=1
    print(count)
counter() # 1
counter() # 2
counter() # 3

def count():
    counter = 0

    def inner_count():
        nonlocal counter
        counter +=1
        # a = 6
        print(counter)
    inner_count()
    # print(a) # нельзя с замкнутого пространства
    return counter
print(count())
print(locals()) # показывает всё, т.к в глобальном пространстве

def func(a):
    print(locals())
func(3) # {'a': 3} | т.к находится в локальном пространстве


a = 7
def func():
    global a
    a+=1

# python ищет переменную - по принципу LEGB