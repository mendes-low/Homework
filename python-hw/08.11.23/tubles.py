# Level 1

# 1
# family = ()

# 2
# family = ('Max' , 'Jonh' , 'Anna' , 'Kate')

# 3
# brothers = ('Max' , 'Jonh')
# sisters = ('Anna' , 'Kate')
# brothers_and_sisters = brothers + sisters
# print(brothers_and_sisters)

# 4
# brothers_and_sisters = ('Max', 'Jonh', 'Anna', 'Kate')
# print(len(brothers_and_sisters))

# 5
# brothers_and_sisters = ('Max' , 'Jonh' , 'Anna' , 'Kate')
# family_members = list(brothers_and_sisters)
# family_members.append('Alex')
# family_members.append('Victoria')
# family_members = tuple(family_members)
# print(family_members)


# Level 2

# 1
# family_members = ('Max' , 'Jonh' , 'Anna' , 'Kate' , 'Alex' , 'Victoria')
# brother1 , brother2 , sister1 , sister2 , parent1 , parent2 = family_members
# print(brother1)
# print(brother2)
# print(sister1)
# print(sister2)
# print(parent1)
# print(parent2)

# 2
# fruits = ('banana' , 'cherry' , 'apple')
# vegetables = ('tomato' , 'potato' , 'onion')
# animal_products = ('beef' , 'egg' , 'honey')
# food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)

# 3
# food_stuff_tp = ('banana', 'cherry', 'apple', 'tomato', 'potato', 'onion', 'beef', 'egg', 'honey')
# food_stuff_lt = list(food_stuff_tp)

# 4
# food_stuff_tp = ('banana', 'cherry', 'apple', 'tomato', 'potato', 'onion', 'beef', 'egg', 'honey')
# print(food_stuff_tp[4])
# print(food_stuff_tp[len(food_stuff_tp)//2])

# 5
# food_stuff_tp = ('banana', 'cherry', 'apple', 'tomato', 'potato', 'onion', 'beef', 'egg', 'honey')
# food_stuff_lt = list(food_stuff_tp)
# print(food_stuff_lt[0:3])
# print(food_stuff_lt[6:])

# 6
# food_stuff_tp = ('banana', 'cherry', 'apple', 'tomato', 'potato', 'onion', 'beef', 'egg', 'honey')
# del(food_stuff_tp)

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('it is in nordic_countries')
else:
    print('it isn\'t in nordic_contries')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if "Iceland" in nordic_countries:
    print('it is in nordic_countries')
else:
    print('it isn\'t in nordic_contries')
