'''
VII. Decision making :

What is Decision Making. Explain different scenarios when to go for Decision Making

Decision making is anticipation(expectation or prediction) of conditions occurring while execution of the
program and specifying actions taken according to the conditions
If else statements are also called decision making statements which are used to execute a block of statement
on certain conditions
If statement is the basic decision-making statement that tells the compiler to execute a code block only if the
condition is true. For example, if the students' marks are above 40, print their results as pass. Otherwise,
print the result as fail
===========================================================================================================
Give examples for below conditions
1. single if : Single if condition is a Boolean expression which results are either TRUE or FALSE, followed by
one or more statements.
2. if else: It also contains a Boolean expression. The if the statement is followed by an optional else
statement & if the expression results in FALSE, then else statement gets executed.
3. if elif else:
4. if elif elif else:
5. Nested if : We can implement if statement and or if-else statement inside another if or if - else statement.
Here more than one if conditions are applied & there can be more than one if within elif.
'''

age = int(input("enter the age : "))
if (age >= 21):
    print("voter")
else:
    print("not voter")
print("end")

marks = int(input("enter the marks : "))
if (marks >= 80 and marks <= 100):
    print("A + grade")
elif (marks >= 60 and marks <=80 ):
    print("A grade")
elif (marks >= 50 and marks <= 60):
    print("B grade")
elif (marks >= 40 and marks <=50):
    print("C grade")
elif (marks >= 35 and marks <=39):
    print("pass")
else:
    print("fail")
print("the end")

a = 40
b = 60
c = 30
if (a > b) and (a > c):
    print("a is a maximum number")
elif (b > a) and (b > c):
    print("b is the maximum number")
else:
    print("c is the maximum number")
print("end")

n = int(input("enter the number : "))
if (n < 0):
    print("negative number", n)
elif (n > 0):
    print("postitive number",n)
else:
    print("zero")
print("end")

i = 10
#if (i == 10):
if (i < 15):
    print("i is smaller than 15")
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
print("the end")


'''
control statements :
break : The break statement is used to terminate the loop or statement .
After that, the control will pass to the statements that are present after the break statement, if available. 
If the break statement is present in the nested loop, then it terminates only those loops which contains
break statement.
continue : 
Continue is also a loop control statement just like the break statement. 
continue statement is opposite to that of break statement, instead of terminating the loop, it forces to 
execute the next iteration of the loop.

pass : 
The pass statement in Python is used when a statement is required syntactically but you do not want any command 
or code to execute.
It is like null operation
'''
for letter in "parvathi":
   if letter == 'v':
      break
   print("Current Letter : ", letter)
print("the end")

for letter in "parvathi":
   if letter == 'h':
      continue
   print("Current Letter : ", letter)
print("hello")

for letter in "sindhura":
   if letter == 'd':
      pass
      print("good morning")
   print("Current Letter : ", letter)

print("Good bye")








