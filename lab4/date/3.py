# Write a Python program to drop microseconds from datetime.
from datetime import datetime

x=datetime.now()
date_format='%d.%m.%Y. %X'
#%X->	Соответствующее время локали
print(x.strftime(date_format))