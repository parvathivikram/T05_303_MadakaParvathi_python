'''
I. Introduction :

tell about Python

Python is a computer programming language, it is used to build websites and software
Python is a general-purpose language, meaning it can be used to create a variety of different programs
=========================================================================================================
why python is so popular today

Python is easy to learn
It uses a simplified syntax with a natural language, for a much easier learning for beginners.
Python is free to use and is supported by large libraries and packages
=========================================================================================================
Features of Python

Easy to Code. Python is a very high-level programming language, but it is easy to understand.
Easy to Read. Python code looks like simple English words.
Free and Open-Source.
Interpreted.
Portable.
Object-Oriented and Procedure-Oriented.
=========================================================================================================
Advantages and Disadvantages of Python

advantages : easy to read and write
             high level language
             user friendly data structure
             open source
             dynamically typed
             object oriented
             interpreted language
             portable across operating systems
disadvantages : slow in speed, python code is executed line by line
                weak in mobile computing and browsers
==========================================================================================================
Interpreted vs Compiled time programming languages. Explain in detail

compile time is the period of time when the programming code is converted to the machine code.
Ru
=========================================================================================================
.py vs .pyc files

.py file contains source code program
.pyc file contains byte code of program
==========================================================================================================
How compilation will happen internally. Explain in detail

The source code in python is saved as . py file which is then compiled into a format known as byte code,
byte code is then converted to machine code.
After the compilation, the code is stored in . pyc files and is regenerated when the source is updated.
=========================================================================================================
Why Python is Dynamically typed programming Language. Explain
Python don't have any problem even if we don't declare the type of variable. It states the kind of variable in the runtime of the program.
Python also take cares of the memory management which is crucial in programming. So, Python is a dynamically typed language.
==========================================================================================================
Python is Platform independent.Explain

Python programs are platform independent because they can be run on different platforms using an interpreter
built for that platform.
============================================================================================================

II. variables :

what is a variable

A Python variable is a symbolic name that is a reference to an object. It is also known as identifier and used
hold the value, it is changeable over time.
============================================================================================================
tokens in Python. Explain all types

A token is the smallest individual unit in a python program. All statements and instructions in a program are
built with tokens
identifiers -  identifier is a name used to identify a variable, function, class, module or other object
keywords - Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name
           or any other identifier.
literals -  defined as raw value or data given in variables or constants.
operators - Operators are special symbols in Python that carry out arithmetic or logical computation.
Punctuators - These are the symbols that used in Python to organize the structures, statements, and expressions.
Some of the Punctuators are: [ ] { } ( ) @  -=  +=  *=  //=  **==  = , etc.
=============================================================================================================
Initializing variable, static,dynamic way

Static variables defined once for the class and shared by all instances.
Dynamic variables defined for individual instances only.
===============================================================================================================
Assigning value to multiple variables. Explain

When assigning multiple variables in a single line, different variable names are provided to the left of
the assignment operator separated by a comma
=============================================================================================================
Garbage collection. How it works internally

python deletes unwanted objects automatically to free the memory space.
when an object is no longer used, the garbage collector reclaims, the underlying memory and reuses it for
future object allocation
==============================================================================================================
Memory Management in Python

memory allocation is allocating block of space in computer memory to a program.
memory allocation and deallocation are done during runtime automatically.
the programmer need not to allocate memory. memory allocation done by python virtual machine
=============================================================================================================
Dynamically typed programming. Explain example

In python no need to declare the type of variable while assigning a value to a variable in Python.
It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language
===========================================================================================================

III. IDE(Integrated Development Environment) pycharm :

Different IDEs in market ?
IDLE
Pycharm
Atom
Jupiter
Spyder
pyDev
=============================================================================================================
Advantages of IDE

An integrated development environment (IDE) is a software suite that consolidates basic tools required to
write and test software.
Developers use numerous tools throughout software code creation, building and testing.
Development tools often include text editors, code libraries, compilers and test platforms.
============================================================================================================
Shortcuts in PyCharm (Explain min 10)

Double Shift - Search Everywhere - Quickly find any file, action, class, symbol, tool window, or setting in
                                   PyCharm, in your project, and in the current Git repository.
Ctrl+Shift+A - Find Action - Find a command and execute it, open a tool window, or search for a setting.
Alt+Enter - Show Context Actions - Quick-fixes for highlighted errors and warnings, intention actions for
            improving and optimizing your code.
F2 - Navigate between code issues
Shift+F2 - Jump to the next or previous highlighted error.
Ctrl+E - View recent files - Select a recently opened file from the list.
Ctrl+W - Extend or shrink selection
Ctrl+Shift+W - Increase or decrease the scope of selection according to specific code constructs.
Ctrl+/ - Add/remove line or block comment
Ctrl+Shift+/ - Comment out a line or block of code.
Alt+F7 - Find Usages - Show all places where a code element is used across your project.
========================================================================================================

IV. operators

Explain in detail about all operators

Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:

Arithmetic operators - Arithmetic operators are used with numeric values to perform common mathematical
operations '''
#addition
x = 23
y = 32
print(x+y)

# substraction
x = -12
y = 59
print(x-y)

# multiplication
x = 12
y = 15
print(x*y)
# division
x = 72
y = 8
print(x/y)
# modulus%
x = 30
y = 10
print(x%y)
# exponentiation**
x = 2
y = 5
print(y**x)
# floor division//)
x = 90
y = 15
print(x//y)
'''Assignment operators - Assignment operators are used to assign values to variables
(=, +=,  -=,  *=, /=, %=, //=, **=, &=)
Comparison operators - Comparison operators are used to compare two values.(==, !=, >, <, >=, <=)
Logical operators - Logical operators are used to combine conditional statements (AND, OR, NOT)
Identity operators - Identity operators are used to compare the objects, not if they are equal, but if they are actually the
same object, with the same memory location (is, is not)
Membership operators - Membership operators are used to test if a sequence is presented in an object(in, not in)
Bitwise operators - Bitwise operators are used to compare (binary) numbers
==========================================================================================================
== vs is

== is for value equality. It's used to know if two objects have the same value. is is for reference equality
============================================================================================================
and or operators. Explain 2 examples

Two or more relations can be logically joined using the logical operators AND and OR.
AND - Returns True if both statements are true. eg : x < 5 and  x < 10
OR - Returns True if one of the statements is true. eg : x < 5 or x < 4
============================================================================================================
operator precedence

This is used in an expression with more than one operator with different precedence to determine which 
operation to perform first.
Example: 10 + 20 * 30
============================================================================================================

V. data types introduction

Importance of DataTypes.

data types are important because the specific data type you use will determine what values you can 
assigning to it and what you can do to it.
============================================================================================================
Different data types, data structures available in Python
   
Data Types - Can hold values and not data, so it is data less
Data structures - Can hold different kind and types of data within one single object
========================================================================================================
 What are CRUD operations.Explain in detail
 
CRUD is acronym for create, read, update and delete
create : The create function allows users to create a new record in the database. create function is called 'insert'.
read : The read function is similar to a search function. It allows users to search and retrieve specific records in the table and read their values
update : The update function is used to modify existing records that exist in the database
delete : The delete function allows users to remove records from a database that is no longer needed
===========================================================================================================
data types - python supports data types they are numbers, string
numbers - integer, float, boolean, complex
int - An integer is a number without a decimal point.
float - A float which means it is a number that has a decimal place.
   Floats are used when more precision is needed.
bool - Boolean is used to represent the true or false value of an expression.
complex - Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j.

======================================================================================================

Explain about string. 
A string is a series of characters. In Python, anything inside quotes is a string. By using either single 
or double quotes we can create string eg : str1 = "sindhu"
Multi line string :
A multiline string in Python begins and ends with either three single quotes or three double quotes. 
Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string. 
Python's indentation rules for blocks do not apply to lines inside a multiline string.
==========================================================================================================


VI. keywords
Explain all keywords with examples and areas of usage
keywords are reserved words in python
  Keywords          Description
=============   ==================
  and	--->   A logical operator
  as	--->  To create an alias
 assert	--->  For debugging
 break	--->  To break out of a loop
 class	--->  To define a class
 continue ---> To continue to the next iteration of a loop
  def	 ---> To define a function
  del	---> To delete an object
 elif	---> Used in conditional statements, same as else if
 else	---> Used in conditional statements
 except	---> Used with exceptions, what to do when an exception occurs
False	---> Boolean value, result of comparison operations
finally	---> Used with exceptions, a block of code that will be executed no matter
             if there is an exception or not
for    --->  To create a for loop
from   --->  To import specific parts of a module
global --->  To declare a global variable
if	---> To make a conditional statement
import	---> To import a module
in      ---> To check if a value is present in a list, tuple, etc.
is	---> To test if two variables are equal
lambda	---> To create an anonymous function
None	---> Represents a null value
nonlocal---> To declare a non-local variable
not	---> A logical operator
or	---> A logical operator
pass	---> A null statement, a statement that will do nothing
raise	---> To raise an exception
return	---> To exit a function and return a value
True    ---> Boolean value, result of comparison operations
try	---> To make a try...except statement
while	---> To create a while loop
with	---> Used to simplify exception handling
yield   ---> To end a function, returns a generator
'''







