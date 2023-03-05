# Write a Python program to count the number 
# of lines in a text file. 

print(sum(1 for line in open('input.txt', 'r')))