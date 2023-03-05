# Write a Python program that invoke square root 
# function after specific milliseconds. Sample 
# Input: 25100 2123 Sample Output: Square root 
# of 25100 after 2123 miliseconds is 
# 158.42979517754858 

import time
import math

sec=int(input())
milisec=int(input())
time.sleep(milisec/1000)

print("Square root of " , sec, "after", milisec , "miliseconds is ", math.sqrt(sec))