# 5.Write a function that accepts string from user 
# and print all permutations of that string.

def permutation(a, l, r):
    if l==r:
        print (a)
    else:
        for i in range(l,r):
            a[l],a[i]=a[i],a[l]
            permutation(a,l+1,r)
            a[l],a[i]=a[i],a[l]
            
s = str(input())
print(permutation(s))

# from itertools import permutations
# def per(s):
#     p = [''.join(p) for p in permutations(s)]
#     return p
# s = str(input())

# print(per(s))