# 12. Define a functino histogram() that takes a 
# list of integers and prints a histogram to the 
# screen. For example, histogram([4, 9, 7]) 
# should print the following:

# ****
# *********
# *******

def histogram(inputList):
    for i in range(len(inputList)):
        print(inputList[i]*'*')
        
a = [int(x) for x in input().split()]
histogram(a)