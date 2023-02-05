#SYNTAX
#Ex1:Insert the 
#missing part of the code below to output "Hello World".
print("Hello World")
#Ex2:This example misses indentations to be correct.
#Insert the missing indentation to make the code correct:
if 5 > 2:
    print("Five is greater than two!")
    
    
#COMMENTS
#Ex1:Comments in Python are written with a special character, which one?
#this is comment
#Ex2:Use a multiline string to make the a multiline comment:
"""
This is a comment
written in 
more than just one line
"""
#VARIABLES

#Ex1
# Create a variable named carname 
# and assign the value Volvo to it.
carname="Volvo"
#Ex2
# Create a variable named x and assign the value 50 to it.
x=50
# Ex3
# Display the sum of 5 + 10, using two variables: x and y
x=5
y=10
print(x+y)
# Ex4
# Create a variable called z, 
# assign x + y to it, and display the result.
x=5
y=10
z=x+y
print(z)
# Ex5
# Remove the illegal characters in the variable name:
# 2my-first_name = "John"
my_second_first_name="John"
myfirst_name="John"
# Ex6
# Insert the correct syntax to 
# assign the same value to all three variables in one code line.
x=y=z="Orange"
# Ex7
# Insert the correct 
# keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x="fantastic"




#DATA TYPES

#Ex1
#The following code example would print
# the data type of x, what data type would that be?
x=5
print(type(x))
#answwer:int

#Ex2
#The following code example would print the data type of x, 
#what data type would that be?
x = "Hello World"
print(type(x))
#answer:str
#Ex3
x = 20.5
print(type(x))
#answer:float
#Ex4
x = ["apple", "banana", "cherry"]
print(type(x))
#answer:list
#Ex5
x = ("apple", "banana", "cherry")
print(type(x))
#answer:tuple
#Ex6
x = {"name" : "John", "age" : 36}
print(type(x))
#answer:dict
#Ex7
x = True
print(type(x))
#answer:bool

# NUMBERS

#Ex1:Insert the 
#correct syntax to convert x into a floating point number.
x=5
x=float(x)
#Ex2
#Insert the correct syntax to convert x into a integer.
x = 5.5
x=int(x)
#Ex3
#Insert the correct syntax to convert x into a complex number.
x=5
x=complex(x)


# STRINGS
#Ex1:Use the len method to print the length of the string.
x="Hello World"
print(x)
#Ex2:Get the first character of the string txt.
txt="Hello World"
x=txt[0]
#Ex3:Get the characters from index 2 to index 4 (llo).
txt="Hello World"
x=txt[2:5]
#Ex4:Return the string without any whitespace at the beginning or the end.
txt="Hello World"
x=txt.strip()
#Ex5:Convert the value of txt to upper case.
txt="Hello World"
txt=txt.upper()
#Ex6:Convert the value of txt to lower case.
txt="Hello World"
txt=txt.lower()
#Ex7:Replace the character H with a J.
txt="Hello World"
txt=txt.replace("H","J")
#Ex8:Insert the correct 
# syntax to add a placeholder for the age parameter.
age=38
txt="My name is John, and I am {}"
print(txt.format(age))

# BOOLEANS
#Ex1:The statement below would print a Boolean value, 
#which one?
print(10>9)
#answer:True
#Ex2:
print(10==9)
#answer:False
#Ex3:
print(10 < 9)
#answer:False
#Ex4:
print(bool("abc"))
#answer:True
#Ex5:
print(bool(0))
#answer:False

# OPERATORS
#Ex1:Multiply 10 with 5, and print the result.
print(10*5)
#Ex2:Divide 10 by 2, and print the result.
print(10/2)
#Ex3:Use the correct membership operator to check 
#if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Ex4:Use the correct comparison operator 
#to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal")
#Ex5:Use the correct logical operator 
#to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")



# if...else
#Ex1:Print "Hello World" if a is greater than b.
a=50
b=10
if a>b:
    print("Hello World")
#Ex2:Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a !=b:
    print("Hello World")
#Ex3:Print "Yes" if a is equal to b, otherwise print "No".
a=50
b=10
if a==b:
    print("Yes")
else:
    print("No")
#Ex4:Print "1" if a is equal to b, 
# print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else: 
    print("3")
#Ex5:Print "Hello" if a is equal to b, and c is equal to d.
if a==b and c==d:
    print("Hello")
#Ex6:Print "Hello" if a is equal to b, or if c is equal to d.
if a==b or c==d:
    print("Hello")
#Ex7:This example misses indentations to be correct.
#Insert the missing indentation to make the code correct:
# if 5 > 2:
# print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
#Ex8:Use the correct 
# short hand syntax to put the following 
# statement on one line:
# if 5 > 2:
# print("Five is greater than two!")
if 5 > 2:print("Five is greater than two!")
#Ex9:Use the correct short hand syntax to write the following 
# conditional expression in one line:
# if 5 > 2: print("Yes")
# else print("No")
print("Yes") if 5>2 else print("No")


