# Write a Python program to copy the contents 
# of a file to another file

a=open('a.txt','r')
z=a.read()
b=open('b.txt','w')
b.write(z)