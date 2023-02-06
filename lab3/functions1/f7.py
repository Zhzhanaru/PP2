# 7.Given a list of ints, return True if the array 
# contains a 3 next to a 3 somewhere.

#     def has_33(nums):
#         pass

#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False
def find_33(a):
    for i in range(len(a)):
        if a[i] == 3 and a[i+1] == 3:
            return True
    return False


a= [int(x) for x in input().split()]
print(find_33(a))


# def has_33(numbs):
#     for i in range(0,len(numbs)-1):
#         if numbs[i:i+2]==[3,3]:
#             return True
#     return False

# print(has_33([1,3,3]))