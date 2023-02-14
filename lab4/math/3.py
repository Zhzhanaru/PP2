# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

from math import tan,pi,floor

num_of_sides=int(input())
length=int(input())
area=floor((num_of_sides*length**2)/(4*tan(pi/num_of_sides)))

print('The area of the polygon is:', area)