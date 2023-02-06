# 10.Write a Python function that takes a 
# list and returns a new list with unique
# elements of the first list. Note: don't 
# use collection set.

def uniq(num):
    unique=[]
    for i in num:
        if i not in unique:
            unique.append(i)
    return unique

a = [int(x) for x in input().split()]
print(uniq(a))
