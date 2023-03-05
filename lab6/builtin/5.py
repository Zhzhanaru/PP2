# Write a Python program with builtin function 
# that returns True if all elements of the tuple 
# are true.

a=tuple(map(int,input().split()))
print(all(a))