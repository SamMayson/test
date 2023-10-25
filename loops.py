"======================Циклы================"
# цикл - это блок кода, который отрабатывает несколько раз 
# for - цикл, который работает с итерируемыми объектами, цикл заканчивает работу, после перебора всех значений итерируемого объекта
# while - цикл, который работает до тех пор, пока условие верно

# while True:
#     print('')
    # будет работать бесконечно

# num1 = int(input('Первое число:'))
# num2 = int(input('Второе число:'))
# operation = input('Выбери операцию: "+, *, /, -, exit"')

# if operation == '+':
#     print(num1+num2)
# elif operation == '-':
#     print(num1-num2)
# elif operation == '*':
#     print(num1*num2)
# elif operation == '/':
#     print(num1/num2)
# elif operation == 'exit':
#     exit()
# else:
#     print('Такой операции нет!')
# play = True

# while play:
#     num1 = int(input('Первое число:'))
#     num2 = int(input('Второе число:'))
#     operation = input('Выбери операцию: "+, *, /, -, exit"')

#     if operation == '+':
#         print(num1+num2)
#     elif operation == '-':
#         print(num1-num2)
#     elif operation == '*':
#         print(num1*num2)
#     elif operation == '/':
#         print(num1/num2)
#     elif operation == 'exit':
#         exit()
#     else:
#         print('Такой операции нет!')
#     one_time = input('Хотите продолжить? yes/no: ')

#     if one_time.lower() == 'yes':
#         play == True
#     elif one_time.lower() == 'no':
#         play == False
#         print('Ещё увидемся!')
#     else:
#         print('Неверный выбор!')

# break - прерывает цикл
# continue - пропускает итерацию (пропускает один цикл)

# string = 'hello world'

# for i in string:
#     if i == 'o':
#         continue
#     else:
#         print(i*2)
# hh
# ee
# ll
# ll
#    - это не "о" принтило, а пробел ' ', тоже символ, вот и там два пробела 
# ww
# rr
# ll
# dd

# nums = list(range(1,101))
# nums2 = []
# for i in nums:
#     if i%2 == 0:
#         continue
#     nums2.append(str(i)+f'{i}')
# print(nums2)

mary = [
    {
        'name': 'Nikita',
        'password': 'gs1'
    },
    {
        'name': 'Nikita',
        'password': 'g1'
    },
    {
        'name': 'Adel',
        'password': '15321'
    },
    {
        'name': 'Adel',
        'password': '51'
    },
    {
        'name': 'Adel',
        'password': '124'
    },
    {
        'name': 'Adel',
        'password': '11'
    },
    ]

play = True
while play:
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    user_found = False

    for user in mary:
        if user['name'].lower() == name.lower() and user['password'] == password:
            print('Login successful!')
            user_found = True
            break

    if not user_found:
        print('User not found or incorrect password.')

    one_more_time = input('Do you want to continue? (yes/no): ')

    if one_more_time.lower() == 'yes':
        play = True
    elif one_more_time.lower() == 'no':
        play = False
        print('Goodbye!')
    else:
        print('Invalid input. Please try again.')



# counter = 0
# for human in mary:
#     if human.get('name') == 'Adel':
#         counter += 1
# print(counter)