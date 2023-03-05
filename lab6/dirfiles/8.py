# Write a Python program to delete file 
# by specified path. Before deleting check 
# for access and whether a given path exists or not.

import os 
path = r'C:\Users\Admin\Desktop\study\2022-2023\Spring 2022-2023\pp2\input.txt' 
if os.path.exists(path): 
    os.remove(path)