# Write a Python program to test whether a given 
# path exists or not. If the path exist find the 
# filename and directory portion of the given path.

import os
path=r'C:\Users\Admin\Desktop\study\2022-2023\Spring 2022-2023\pp2\lab6\dirfiles' 

if os.path.exists(path):
    print(os.path.exists(path)) 
    print(os.path.basename(path)) 
    print(os.path.dirname(path))