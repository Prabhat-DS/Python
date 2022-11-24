# 1. Write a Python program to print "Hello Python"?
print("Hello Python")


# 2. Write a Python program to do arithmetical operations addition and division.?
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print("addition of two number(num1 +num2): ", num1+num2)
print("division of two number(num1 /num2): ", num1/num2)


# 3. Write a Python program to find the area of a triangle?
p=int(input("enter length of perpendiculer in meter: "))
b=int(input("enter lenth of base in meter : "))
area= 0.5*b*p
print("area= 1/2 * b * p = ", area, "sqm")


# 4. Write a Python program to swap two variables?
ver1= 5
ver2= 6
print("ver1=" ,ver1)
print("ver2=" ,ver2)
ver1, ver2 = ver2, ver1
print("after swaping ")
print("value of ver1: " ,ver1 )
print( "value of var2: " ,ver2)


# 5. Write a Python program to generate a random number?
import random
print(random.randint(0,9))


