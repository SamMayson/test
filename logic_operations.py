"======================Логические и условные операторы===================="
# логические операторы - выражения, которые возвращают True, если вырожение верно или же False, если выражение не верно

# равеноство
5==5 # True
4==5 # False

# не равенство
4!=4 # False
4!=5 # True

#  больше
5>4 # True
4>5 # False
5>5 # False

# меньше
4<5 # True
4<4 # False
4<2 # False

# больше или равно
4>=10 # False
4>=4 # True
10>=7 # True

# меньше или равно
10<=5 # False
10<=10 # True
5<=10 # True

'5'=='5' # True
'5'==5 # False
'hello'=='hello' # True
'Hello'=='Hello' # True
'Hello'=='hello' # False

"============And or Not============="
# and - и
# or - или
# not - не

a = 5
b = 6

# True and True
a == 5 # True 
a == 5 and b == 6 # True
# True and False
a == 5 and b == 7 # False
# False and False
a == 4 and b == 1 # False

a == 5 or b == 6 # True
a == 5 or b == 7 # True
a == 4 or b == 4 # False

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True

# is | --

not 5==5 and 6 == 6 # False
not 5==5 and 7==0 # True
not 7>=5 or 6<=4 # False
not not not True # False

"==============Bolean Type================"
# Булевый тип данных имеет всего 2 значения True и False

bool(1) # True
bool(5) # True
bool(0) # False
bool(-22) # True

bool('') # False
bool(' ') # True
bool('hello') # True

bool(True) # True
bool(False) # False
bool('False') # True
bool('True') # True
bool([]) # False
bool([[]]) # True

"==============Non Type========="
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствуия значения
bool(None) # False
bool('None') # True

a = None
a == None # True

'hello world' == 'hello' # False
'hello' in 'hello world' # True
'hello' > 'hell' # True
'hello' > 'hellw' # False

"=================Условные операторы============"
# условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному
# (в зависимости от условия)


# надо принять от пользователья число если число отрицательное то ваша программа вывести в терминал сообщение 'NEGATIVE', а если число положительное то 'POSITIVE' а если 0 то 'ZERO'

num = int(input("Введите число: "))

if num < 0:
    print("NEGATIVE")
elif num > 0:
    print("POSITIVE")
else:
    print("ZERO")

"===============Тернарные операторы==========="
# тернарные операторы - условие в одну строчку
# тело1 if условие else тело2
# принять число от пользователя число если число = 5 то выводим hello, в ином случае выводим bye
num1 = int(input("сюда: "))
result = "hello" if num1 == 5 else "bye"
print(result)

# примите число от пользователя
# выведите Fizz, если число кратно 3
# выведите Buzz, если число кратно 5
# выведите FizzBuzz, если число кратно и 3, и 5
# выведите число во всех остальных случаях

username = 'Sam'
password = '123321'

input_username = input('Введите логин: ')
input_password = input('Введите пароль: ')

if input_username.lower() == username.lower() and input_password == password:
    print('Успешно!')
else:
    print('Не удача!')