# 2.Read in a Fahrenheit temperature. 
# Calculate and display the equivalent centigrade 
# temperature. The following formula is used for 
# the conversion: C = (5 / 9) * (F – 32)
def secondfunc(f):
    return (5 / 9) * (f - 32)
f = int(input())
print(secondfunc(f))

# 86->30
# 100->37.79