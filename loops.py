'''
Explain below terms in detail
Requirement :

User Criteria
Validations(Client vs Server)
=============================================================================================================
State vs Behavior .

State simply means data or value.
Behavior means action or work or task or operation that the object does.
============================================================================================================
Loops :

Importance of Loops

Looping means repeating something over and over until a particular condition is satisfied.
Without the loop structure in a computer program, the tasks are almost impossible to be performed.
Loops, on the one hand, execute the tasks faster saving the time and energy, on the other hand, they are
very helpful to accomplish the tasks in an accurate manner.
===========================================================================================================
while loop. Explain in detail with different use cases

The while loop in Python is used to iterate over a block of code as long as the test expression/condition is true.
We generally use this loop when we don't know the number of times to iterate beforehand
===========================================================================================================
for loop. Explain in detail with different use cases

For loop in python is used to execute a block of statements or code several times until the given condition
becomes false.
We use the for loop when we know the number of times to iterate.
==========================================================================================================
while vs for

The for statement iterates through a collection or iterable object or generator function. The while statement
simply loops until a condition is False.
=============================================================================================================
Give examples while with if else combination

The else part is executed if the condition in the while loop evaluates to False .
The while loop can be terminated with a break statement. In such cases, the else part is ignored.
Hence, a while loop's else part runs if no break occurs and the condition is false.
============================================================================================================
'''
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('current fruit:', fruits[index])
print('good bye')

fruits = ['banana', 'apple', 'mango', 'papaya', 'guava']
for fruit in fruits:
    print('current fruit:', fruit)
    for char in fruit:
        print("char if fruit", char)
print("good bye")

count = 0
while (count < 9):
    print('the count is:', count)
    count = count + 1
print("hello world")

# while with if
x = 1
while x <= 100:
    x += 1
    if x % 3 == 0 and x % 5 == 0:
        print(x)
print("hai")

lower = int(input("enter the lower : "))
upper = int(input("enter the upper : "))
n = int(input("enter the divisible by : "))
for i in range(lower, upper + 1):
    if (i % n == 0):
        print(i)
print("end")

