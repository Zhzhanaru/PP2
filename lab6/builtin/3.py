# Write a Python program with builtin 
# function that checks whether a passed 
# string is palindrome or not.

str=input()
str_reverse=''.join(reversed(str))
if str_reverse==str:
    print('Yes,it is a palindrom')
else:
    print('No,it is not a palindrom')