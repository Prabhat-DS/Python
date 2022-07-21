''' 1.What are the two values of the Boolean data type? How do you write them?'''
# True and False are the two boolean data type.
t= True
f= False
print("print the type of True: ",type(t))
print("print the type of False: ",type(f))
print("4>3 is: ",4>3)
print("3>4 is: ",3>4)

'''# 2. What are the three different types of Boolean operators?'''
# AND , OR and NOT are three diffrent boolean operator( logical operators).
# and-operator thro the True when vallue all the is true. (True and True = true)(it work as a multiplication of two variable)
# or-operator thro the True when vallue if the vallue of any one is True. (true and False = true)(it work as a addition of two variable)
# not-operator reverse true-value ti false or vise versa (true and true = true).


'''3. Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).'''
print("Truth table of 'and' operator for two variables: \n",
      "1    1 : ", 1 and 1, "\n",
      "1    0 : ", 1 and 0, "\n",
      "0    1 : ", 0 and 1, "\n",
      "0    0 : ", 0 and 0)
print("Truth table of 'or' operator for two variables: \n",
      "1    1 : ", 1 or 1, "\n",
      "1    0 : ", 1 or 0, "\n",
      "0    1 : ", 0 or 1, "\n",
      "0    0 : ", 0 or 0)
print("Truth table of 'not' operator for two variables: \n",
      "1 : ", not 1, "\n",
      "0 : ", not 0)

'''4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)'''
print("1:",(5 > 4) and (3 == 5))
print("2:",not (5 > 4))
print("3:",(5 > 4) or (3 == 5))
print("4:",not ((5 > 4) or (3 == 5)))
print("5:",(True and True) and (True == False))
print("6:",(not False) or (not True))

# 5. What are the six comparison operators?
print ("six comparision operators are: > , <, >= , <=, ==, !=  " )

'''6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.'''
# 'equal to (==)' is a comparision operator which return the boolean value as True(1) and Fauls(0), it check the two operands are equal or not, if equal it return true else false.
# assignment operator is used for the assign the value on the right side to the variables in left side.
# example:-
print("example of equal to(==) operator: 4<5",4<5 )
print ("example of assignment operator: ")
x = 20
y = "shsjkfhs"
z = 20.30
print("x=",x, " y=",y , " z=",z)


'''7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')'''
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
# in this code there is two if-block and one is else block

'''8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.'''
span = int(input("enter any number: "))
if span == 1:
    print("hello")
elif span == 2:
    print("Howdy")
else:
    print("Greetings!")


'''9.If your programme is stuck in an endless loop, what keys you’ll press?'''
# a= 1
# while a >=1:
#     print("to intrrupet the loop press 'ctrl + F2'")


'''10. How can you tell the difference between break and continue?'''
# break statment used to come out from the loop when the condition is sertisfied.
# continue statment used to skip the perticular condition and move on to the next itteration.
print("example of  break statment")
for i in range(1, 10):
    if i ==5:
        break
    print(i)
    i=i+1
print("example of  continue statment")
for i in range(1, 10):
    if i ==5:
        continue
    print(i)
    i=i+1

'''11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?'''
# there is no workin defrence between range(10), range(0, 10), and range(0, 10, 1).
# range(10):- start value is by default 0 and range up to 9
# range(0, 10):- start value is defind as 0 and range up to 9
# range(0, 10, 1):- start value is defind as 0 and range up to 9 with the jump of 0.
print("11:-example of range funtion")
for i in range(10):
    print(i)
for i in range(0,10):
    print(i)
for i in range(0,10,1):
    print(i)

'''
12. Write a short program that prints the numbers 1  to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.'''
print("12:-program to print 1 to 10 using for loop")
for i in range(1,11):
    print(i)


print("12:-program to print 1 to 10 using while loop")
i=1
while i<=10:
    print(i)
    i+=1

'''13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?'''
# 1st method
# import spam
# spam.bacon()

# 2nd method
# import spam as sp
# sp.bacon()

# 3rd method
# from spam import *
# bacon()