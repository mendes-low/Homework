# Level 1

# 1
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# print(len(it_companies))

# 2
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.add('Twitter')
# print(it_companies)

# 3
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.update(['Youtube' , 'WhatsApp' , 'Telegram'])
# print(it_companies)

# 4
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.remove('IBM')
# print(it_companies)

# 5
# Ошибка шықпайды
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.discard('Telegram')
# print(it_companies)

# Ошибка шығады
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.remove('Telegram')
# print(it_companies)


# Level 2

# 1
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.union(b))

# 2
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.intersection(b))

# 3
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.issubset(b))

# 4
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.isdisjoint(b))

# 5
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.union(b))
# print(b.union(a))

# 6
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# print(a.symmetric_difference(b))

# 7
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# del a
# del b


# Level 3

# 1
# age = [22 , 19 , 24 , 25 , 26 , 24 , 25 , 24]
# print(len(age))
# print(len(set(age)))
# print(len(set(age)) < len(age))

# 2
# String = '''
# Strings are an integrable data structure. 
# There are two ways to iterate over the elements of strings by characters and by indexes. 
# Each element of the string is represented by one character. 
# Strings are an immutable data structure.
# '''

# List = '''
# Lists are ordered. 
# The list item can be accessed by index. Lists are mutable types. 
# The list can store the number of different elements.
# '''

# Tuble = '''
# Tuples in Python are the same lists with one exception. 
# Tuples are immutable data structures. 
# Just like lists, they can consist of elements of different types, separated by commas.
# Tuples are enclosed in round brackets, not square brackets.
# '''

# Set = '''
# Set is an unordered collection of unique elements. 
# Unique, that is, there are no duplicate values in it.
# '''

# 3
# sentence = 'I am a teacher and I love to inspire and teach people'
# sentence_set = sentence.split()
# sentence = set(sentence_set)
# print(sentence)


