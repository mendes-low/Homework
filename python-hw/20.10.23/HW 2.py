#1
# import random
# numbers = random.sample(range(50) , 10)
# print(numbers)
# max_number = input("Показать самое максимальное число в списке ?")  
# max_number = max(numbers)
# print(f"Максимальное число:{max_number}")
# mean_number = input("Показать среднее число в списке ?")
# mean_number_sum = sum(numbers)
# mean_number_len = len(numbers)
# mean_number = mean_number_sum / mean_number_len
# print(f"Среднее число:{mean_number}")
# min_number = input("Показать минимальное число списке ?")
# min_number = min(numbers)
# print(f"Минимальное число:{min_number}")
# search = input("Поиск числа в списке:")
# while numbers != search:
#     print("Это число нет в списке")
# else:
#     print("Это число есть в списке")

#2
# import random
# numbers = []
# for i in range (0,6):
    # number = random.randint(1,50)
    # while number in numbers:
        # number = random.randint(1,50)
    # numbers.append(number)
# numbers.sort()
# user = []
# for i in range(0,6):
    # number = int(input("Введите число от 1 до 50:"))
    # while (number in user or number <1 or number >50):
        # print("Введите число снова:")
        # number = int(input("Введите число от 1 до 50:"))
    # user.append(number)
# print(f"Числа лотереи:{numbers}")
# print(f"Числа участника:{user}")
# result = 0
# for number in user:
    # if number in numbers:
        # result =+ 1
# print(f"Cовпало чисел:{str(result)}")

#3
# start = input("Хотите начать программу 'Список дел'?")
# if start == "да":
#     for i in range(1,100):
#       print(f"Добро пожаловать в программу 'Список дел'")
#     choices = ["1.Добавить пункт в список" , "2.Удалить пункт из списка" , "3.Просмотреть список" , "4.Завершить работу"]
#     add = []
#     for choice in choices:
#         choice2 = int(input("Введите ваш выбор (1/2/3/4):"))
#     if choice2 == 1:
#         add2 = input("Добавить товар:")
#         add.append(add2)
#         print(f"В список добавлен пункт:{add2}")
#         print(add)
#     elif choice2 == 2: 
#         delete = input("Удалить пункт:")
#         for delet in add:
#            if delet ==  add:
#                add.remove(delet)
#                print(add)         
# else:
#     print("Хорошо,удачи тебе")    


# #4
# number = int(input("Введите число:"))
# for numb in range(1,11):
#     print(f"{number} * {numb} = {number * numb}")

