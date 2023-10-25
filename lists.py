"================Список============"
# список - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, 
# предназначенный для хранения любых данных в определенном порядке

list1 = [1, 2, 3, 'hello', [2, 0, 0.2], None, True, False]
list1[3] # hello
print(list1[3][-1]) # o
list1[-1] # False
list1[4] # 2, 0, 0.2
list1[4][1] # 0

list2 = list("hello")
['h', 'e', 'l', 'l', 'o']

list3 = list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list4 = [1] * 5
[1, 1, 1, 1, 1]

list5 = list(range(1, 12, 2))
[1, 3, 5, 7, 9, 11]

# string = 'hello'
# string.upper()
# print(string) # hello

"====================Методы списков============"
# .append добавляет данные всегда в конец списка
list1 = []
list1.append(1) 
print(list1) # [1]
list1.append('hello') 
print(list1) # [1, 'hello']
list1.append([1,2,3])
print(list1) # [1, 'hello', [1,2,3]]

# pop - удалаяет элемент из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), 
# если не передать индекс - удалит с конца
list1 = [1,2,3,4,5,6]
print(list1.pop(2)) # 3
print(list1) # [1, 2, 4, 5, 6]

list1 = [1,2,3,4,5,6]
popped = list1.pop(2)
print(list1, popped) # [1, 2, 4, 5, 6] 3

# если список пустой, то при удалении выйдет IndexError
# list1 = []
# list1.pop()
# print(list1)
# IndexError (нет чего возвращать)

# remove - удаляет по значению (первый найденный элемент)
list1 = [1,2,'hello',4,5,6]
list1.remove('hello')
print(list1) # [1, 2, 4, 5, 6]

list1 = [1,2,'hello',4,5,6]
removed = list1.remove('hello')
print(list1, removed) # [1, 2, 4, 5, 6] None

list1 = [1] * 4
list1.remove(1)
print(list1) # [1, 1, 1]

# count
list1 = [1, 1, 1, 1, 1, 1, 2, 3, 4, 1]
counter = list1.count(1)
print(counter) # 7

list1 = ['hello', 'hello', 'hello']
counter = list1.count('hello')
counter1 = list1.count('h')
print(counter) # 3
print(counter1) # 0

# insert - добавляет элемент в список по индексу
list1 = [1,2,3,4,5,6]
list1.insert(0, 'hello')
print(list1) # ['hello', 1, 2, 3, 4, 5, 6]

# extend - добавляет элементы принятого распакуемого обьекта в список
list1 = [1,2,3]
list1.append([4,5,6]) # [1,2,3,[4,5,6]]
list1.extend([4,5,6]) # [1,2,3,4,5,6]
list1.extend('hello') # [1,2,3,'h','e','l','l','o']

# reverse
listr = [1,2,3]
listr.reverse()
print(listr)

# sort - сортирует список, состоящий из элементов одного типа данных
list1 = [3,2,1,5,5,7,3]
list1.sort()
print(list1) # [1, 2, 3, 3, 5, 5, 7]

list1 = ['a', 'd', 'b', 'c']
list1.sort()
print(list1) # ['a', 'b', 'c', 'd']

# list1 = [1,'b','a', '2']
# list1.sort()
# print(list1) # TypeError | Only int or str

"================For=============="

# цикл - блок кода который отробатывает несколько раз

list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1: # i - можно заменить на любое удобное название
    print(i)
list1 = ['a', 'b', 'c', 'c4']
for i in list1:
    print(i)

list1 = [1,2,3,4,5,6,7,8,9,10]
# list1 = list(range(1,256))
for i in list1: # i - можно заменить на любое удобное название
    if i % 2 == 0:
        print(i) # выводит только четные числа из списка list1. В данном случае, вывод будет: 2, 4, 6, 8, 10.

# надо создать диапозон чисел от 1 до 255, если число четное, то мы добовляем в новый список четное число, а если число не четное, то мы выводим такой текст: "чача мачача". В конце мы должны вывести список с четными числами

super = []
for i in range(1,256):
    if i % 2 == 0:
        super.append(i)
    else:
        print("чача мучача")
    print(super)

given_list = list(range(1,256))
new_list = []
for num in given_list:
    if num % 2 == 0:
        new_list.append(num)
    else:
        print("чача мучача")
    print(new_list)