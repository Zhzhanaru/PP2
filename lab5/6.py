# Write a Python program to replace all 
# occurrences of space, 
# comma, or dot with a colon.

import re

s = input()
x = re.sub('[\s+]', ',', s)
print(x)
