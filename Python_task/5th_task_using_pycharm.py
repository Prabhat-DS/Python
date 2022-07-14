# function task :
#     q1 : Try to print a prime number in between 1 to 1000
#     q2 : Try to write a function which  is equivalent  to print function in python
#     q3 : Try to write a function which is a replica of list append , extend and pop function
#     q4 : Try to write a lambda function which can return a concatination of all the string that we will pass
#     q5 : Try to write a lambda function which can return list of square of all the data between 1-100
#     q6 : Try to write a 10 Different different example of lambda function with a choice of your taks
#     q7 : Try to wwrite a funtion whihc can perform a read operation from .txt file

#         shivan@ineuron.ai
#         sudhashu@ineuron.ai

# =========================================================================================================
#     q1 : Try to print a prime number in between 1 to 1000
l = []
def prime(a):
    for num in range(1, a + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                l.append(num)
    print(l)
prime(1000)
# =========================================================================================================
#   q2 : Try to write a function which  is equivalent  to print function in python

l=[]
def pr(a):
    for i in a:
        l.append(i)
    s=""
    for j in l:
        s=s+j
    print(s)

pr("zdvfsfsfssdf")

#========================================================================================================
# q3 : Try to write a function which is a replica of list append , extend and pop function
l2 = [1,2,3,5]
l3= [4,5,6,8]
print(len(l2))
def ap(a):
  l2.append(int(input("any number u want to append in list l2: ")))
  print(l2)
  l2.extend(l3)
  print(l2)
  print(l2.pop(int(input("enter the number u want to remove from list: "))))
ap(l2)


# ========================================================================================================
# q4 : Try to write a lambda function which can return a concatination of all the string that we will pass
# Concatenation, in the context of programming, is the operation of joining two strings together.

con= lambda *a: ''.join(a)
con("shdaskdgksa"+"kumar")


# =========================================================================================================
#     q5 : Try to write a lambda function which can return list of square of all the data between 1-100
sqr=lambda a: print(a*a)
l=[2,3,5,8,22,33,44,55,66,88,98,100,102,105,200,500,1000]
for i in l :
  if i<=100:
    sqr(i)


# ===========================================================================================================
#     q6 : Try to write a 10 Different different example of lambda function with a choice of your taks
a1=lambda a: a+10
a2=lambda **x : x
a3=lambda x : x**2
a4 = lambda x : pow(x,x) + x**2
a5 = lambda x : chr(x)
a6 = lambda x,y : x**y
a7 = lambda *x : ''.join(x)
a8 = lambda *x : [i**i for i in x ]
a9 = lambda *x : [i*2 != 0 for i in x]
a10 = lambda *x : [i>1000 for i in x]

#  q7 : Try to write a funtion whihc can perform a read operation from .txt file
import os

readtxt = lambda x: (open(x)).readline
readtxt("hello.txt")
