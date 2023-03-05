# Write a Python program to check for access 
# to a specified path. Test the existence, 
# readability, writability and executability 
# of the specified path 

import os  

path = r'C:\Users\Admin\Desktop\study\2022-2023\Spring 2022-2023\pp2\lab6\dirfiles\input.txt'
path1 = os.access(path, os.F_OK) 
print("Exists the path:", path1) 
path2 = os.access(path, os.R_OK) 
print("Access to read the file:", path2) 
path3 = os.access(path, os.W_OK) 
print("Access to write the file:", path3) 
path4 = os.access(path, os.X_OK) 
print("Check if path can be executed:", path4)