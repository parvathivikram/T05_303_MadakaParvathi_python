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