# 4.You are given list of numbers separated by 
# spaces. Write a function filter_prime which 
# will take list of numbers as an agrument and 
# returns only prime numbers from the list.
def filter_prime(n):
    if(n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

# print(filter_prime(9))
# print(filter_prime(7))
a = [int(x) for x in input().split()]
y=[]
print(a)
filter_prime(a, y)
print(y)