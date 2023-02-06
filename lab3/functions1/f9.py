# 9. Write a function that computes 
# the volume of a sphere given its radius.
def volume(r):
    vol=(4/3)*3,14159*(r**3)
    return vol

r = float(input())
print(volume(r))
