# Write a Python program to write a list to a file.

arr=[1,2,3,4,5,10,11,12,23,22]

with open('input.txt','w') as f:
    for i in arr:
        f.write("%s\n" %i)