"===============Comprehesions============="
# comprehesion - генератор, с помощью которого мы можем создать последовательность, используя цикл for в одну строчку

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтрация

comprehesion = (i for i in range(1,6))
# генератор - итерируемый объект, который не хранит в себе полносью всю последовательность, а создает их когда требуется

for i in comprehesion:
      print(i)
      print(i, end='|')

print(comprehesion) # <generator object <genexpr> at 0x10265d660>
print(next(comprehesion)) # 1
print(next(comprehesion)) # 2
print(next(comprehesion)) # 3
print(next(comprehesion)) # 4
print(next(comprehesion)) # 5
# print(next(comprehesion)) # StopIteration

#  next - функция, которая запрашивает у генератора текущий элемент и генератор создает элемент

"===================Синтаксический сахар==============="

list_comprehesion = list(i for i in range(1,6))
print(list_comprehesion) # [1, 2, 3, 4, 5]

list_comprehesion = [i for i in range(1,6)]
print(list_comprehesion) # [1, 2, 3, 4, 5]

list_comprehesion = list(i for i in range(1,6) if i%2==0)
print(list_comprehesion) # [2, 4]

# с использованием comprehesions создать список не четных чисел в диапозоне от 1 до 100 включительно,
list_comprehesion = list(i for i in range(1,101) if i%3==0)
print(list_comprehesion) 
result = [i for i in range(1,101,2)] # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
result = [i for i in range(1,101) if i%2!=0] # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

result = ["hello" for i in range(5)]
print(result)

result = []
for i in range(5):
    result.append('hello')
print(result)

# с использованием comprehesions создать список чисел в диапозоне от 1 до 100, если число кратно 3 оставляет в списке fizz, 
# в инном случае оставляет просто число
result = ['fizz'if i%3==0 else i for i in range(1,101)]
print(result)

result = []
for i in range(1,101):
    if i%3==0:
        result.append('fizz')
    else:
        result.append(i)
print(result)

matrix = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]
result = [j for i in matrix for j in i]
print(result) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

result = []
for i in matrix:
    for j in i:
        result.append(j)
print(result) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

"=================Set comprehesion============="

result = {i for i in range(1, 11)}
print(result) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

result = {i if i%2==0 else i*2 for i in range(1,21)}
print(result) # {2,4,6,......}

# если условие находится в начале то это тернарные условия (добавляется оператор else)
# если условие в конце то это фильтрация (не добавляется else)

"=================Dict comprehensions=========="
{1:1, 2:4}
dict_ = {}
for i in range(1,11):
    dict_.update({i:i**2})
print(dict_) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

result = {i:i**2 for i in range(1,11)}
print(result) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# дается список [1,1,2,2,2,4,4,4,4,4]
# надо посчитать количество значений в списке и записать в новый словарь в качестве значения количетсво повторений элемента

list_ = [1,1,2,2,2,4,4,4,4,4]
dict_ = {}
for i in list_:
    dict_.update({i:list_.count(i)})
print(dict_) # {1: 2, 2: 3, 4: 5}

list_ = [1,1,2,2,2,4,4,4,4,4]
dict_ = {i:list_.count(i) for i in list_}
print(dict_) # {1: 2, 2: 3, 4: 5}

dict_ = {'a':2, 'b':3}
dict_ = {key:val for key, val in dict_.items()}
dict__ = {val:key for key, val in dict_.items()}
print(dict_) # {'a': 2, 'b': 3}
print(dict__) # {2: 'a', 3: 'b'}

# дается словарь {'a': 2, 'b': 3}, нужно создать новый словарь в котрром будет лежать
# {'a': 'четное', 'b': 'нечетное'}
dict_ = {'a': 2, 'b': 3}
new = {key:'четное' if val%2==0 else 'нечетное' for key, val in dict_.items()}
print(new) # {'a': 'четное', 'b': 'нечетное'}

dict_ = {'a': 2, 'b': 3}
dict2 = {}
for key, val in dict_.items():
    if val%2==0:
        dict2.update({key:'четное'})
    else:
        dict2.update({key:'нечетное'})
print(dict2) # {'a': 'четное', 'b': 'нечетное'}