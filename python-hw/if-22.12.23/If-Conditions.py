# Level 1

# 1 (1 part)
# age = int(input('Enter your age: '))
# if age < 18: 
#     if age < 0:
#         print('Error')
#     else:
#         print(f'You need {18 - age} more years to learn to drive.')
# else:
#     print('You are old enough to drive')

# 1 (2 part)
# age = int(input('Enter your age: '))
# if age > 0 and age >= 18:
#     print('You are old enough to drive')
# elif age > 0 and age < 18:
#     print(f'You need {18 - age} more years to learn to drive.')
# else:
#     print('Error')

# 2
# my_age = 16
# your_age = int(input('Enter your age: ')) 
# if your_age > my_age:
#     if your_age - my_age == 1:
#         print('You are 1 year older than me')
#     else:
#         print(f'You are {your_age - my_age} years older than me')    
# else:
#     print(f'You are {my_age - your_age} years younger than me')
    
# 3
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# if a > b:
#     print(f'{a} is greater than {b}')
# elif b > a:
#     print(f'{b} is greater than {a}')
# else:
#     print('They are equal')


# Level 2

# 1
# grade = int(input("Оценка теста:"))
# if grade >= 80 and grade >= 100:
#     print("A")
# elif grade >= 70 and grade >= 79:
#     print("B")
# elif grade >= 60 and grade >= 69:
#     print("C")
# elif grade >= 50 and grade >= 59:
#     print("D")
# elif grade >= 0 and grade >= 49:  
#     print("F")  
# else:
#     print("Error")

# 2
# season = input('Enter month: ')
# if season == 'September' and season == 'October' and season == 'November':
#     print('That time of year is Autumn')
# elif season == 'December' and season == 'January' and season == 'February':
#     print('That time of year is Winter')
# elif season == 'March' and season == 'April' and season == 'May':
#     print('That time of year is Spring')
# elif season == 'June' and season == 'July' and season == 'August':
#     print('That time of year is Summer')
# else:
#     print('It is not mouth')

# 3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Enter friut: ')
# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(f'We have added the fruit to the list:{fruits}')


# Level 3

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# 1
# if ('skills' in person):
#     print(person['skills'][len(person['skills'])//2])
# else:
#     print('skills is not in person')

# 2
# if ('skills' in person):
#     if 'Python' in person['skills']:
#         print('Python' in person['skills']) 
# else:
#     print('skills is not in person')

# 3
# if 'JavaScript' and 'React' in person['skills']:
#     print('He is a front end developer')
# elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
#     print('He is a backend developer')
# elif 'React' and 'Node' and 'MongoDB' in person['skills']:
#     print('He is a fullstack developer')
# else:
#     print('he is a nobody')

# 4
# if person['country'] == 'Finland' and person['is_marred'] == True:
#     print(f'Asabeneh Yetayeh lives in {person["country"]}. He is married.')
# else:
#     print('He is nobody')
