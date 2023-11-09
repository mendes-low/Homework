# 1
# num = int(input("Enter a number: "))
# p = True
# for i in range(2,num):
#   if(num%i == 0):
#     p = False
#     break
# if p == True:
#   print(f"{num} is a prime number")
# else:
#   print(f"{num} is not a prime number")

# 2
# import math

# num = int(input("Number 1:"))
# num2 = int(input("Number 2:"))
# print(math.gcd(num,num2))

# 3
# num = int(input("Enter:"))
# num2 = int(input("Enter power:"))
# result = num**num2
# print(result)

# 4
# import math 

# calculator = int(input("Write a positive number: "))
# print(math.sqrt(calculator))

# #5
# import math

# a = int(input("Write the length A: "))
# b = int(input("Write the length B: "))
# c = int(input("Write the length C: "))
# p = (a+b+c)/2
# S = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f"area of a triangle {S}")

# #6
# C = float(input("Write the radius of the circle: "))
# S = 3.14*(C**2)
# print("area of a circle: ", S)

# 7
# fib1 = 1
# fib2 = 1
# n = int(input("Enter number Fibonachi:"))
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
# print(f"The meaning of this number:{fib2}")

# # 8
# a = int(input("Enter:"))
# r = int(input("Enter:"))
# t = int(input("Enter:"))
# y = a*(1 + r)**t
# print(y)

# 9
# import math 

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# D = b**2 - 4*a*c
# if D > 0: 
#     x1 = (- b + math.sqrt(D))/(2*a)
#     x2 = (- b - math.sqrt(D))/(2*a)
#     print(f"x1={x1}")
#     print(f"x2={x2}")
# elif D == 0:
#     x = -b/(2*a)
#     print(f"x={x}")
# else:
#     print(f"The equation has no real roots")

# num = int(input("Enter:"))
# num2 = int(input("Enter power:"))
# result = num
# for i in range(1,num2):
#     result = result * num2
# print(result)
