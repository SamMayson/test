"======================Словари============="
# dict - изменяемый, итерируемый, неидексируемый, неупорядоченный тип данных, где данные хранятся в парах(ключ:значение)

user = {
        'name':'Sam',
        'password': '123',
        'last_name': 'Veretennikov'
        }
print(user['name'])

# ключами в словаре могут быть, только не изменяемые типы данных

dict1 = {'a':1, 'b':1, 'a':5, 'a':6}
print(dict1['a']) # 6
# если ключи одинаковые, сохраняется только последнее значение

# print(dict1['c']) # KeyError: 'c'

"===============Создание============"
dict1 = {'a':'hello'}
dict1 = dict([('a','hello')]) # {'a':'hello'}
dict2 = dict(["ab", "cd"]) # {'a': 'b', 'c': 'd'}
#print(dict1)
dict1 = {}
dict1['name'] = 'Sam'
# {'name':'Sam'}
dict1['name'] = 'Tima'
# {'name':'Time'}
"KISS" # keep it simple, stupid

"===============Методы словоря============="
# get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение
user = {
        'name':'Sam',
        'password': '123',
        'last_name': 'Veretennikov'
        }
print(user['password']) # 123
print(user.get('test')) # None
print(user.get('test', 'чо')) # чо

# pop - удаляет пару по ключу и возвращает значение
dict1 = {'a':1, 'b':2}
popped = dict1.pop('a')
print(dict1, popped) # {'b': 2} 1
del dict1['b']
print(dict1) # {}

# popitem - удаляет последнюю пару и возвращает её
dict1 = {'a':1, 'b':2}
popped = dict1.popitem()
print(dict1, popped) # {'a': 1} ('b', 2)

# update - добавляет новую пару, если есть существующа] пара, то он заменяет ее
dict1 = {1:'a', 2:'b', 3:'c'}
dict1[4] = 'd'
dict1.update({5:'e'})
print(dict1)

# clear - очищает словарь
dict1 = {1:'a', 2:'b', 3:'c'}
dict1.clear
print(dict1) # {}

# .keys() - возвращает все ключи
# .values() - возвращает все  значения
# .items() - возвращает все пары

user = {
        'name':'Sam',
        'password': '123',
        'last_name': 'Veretennikov'
        }

"===============Итерирование словарей============"

user = {
        'name':'Sam',
        'password': '123',
        'last_name': 'Veretennikov'
        }
for key in user:
    print(key)
    # при итерации словаря будут только ключи
for values in user.values():
    print(values)
    # при итерации dict-values будут приходить значения
for key, values in user.items():
    # при итерации dict_items будут приходить и ключи и значения в виде tuple
    print(key, values)

# вам дан словарь
# {'a':1, 'b':2, 'c':3}
# создайте новый словарь в котором надо поменять местами ключ и значение
# {1:'a', 2:'b', 3:'c'}

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {}
for key, value in dict1.items():
    dict2.update({value:key})
print(dict2) # {1: 'a', 2: 'b', 3: 'c'}