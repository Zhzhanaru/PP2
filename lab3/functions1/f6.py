# 6.Write a function that accepts string from user, 
# return a sentence with the words reversed. 
# We are ready -> ready are We
def revers_sentence(x):
    x.reverse()
        
s = str(input())
x = s.split()
revers_sentence(x)
r = ' '.join(str(x) for x in x)
print(r)









# def reverseword(s, start, end):
#     while start<end:
#         s[start],s[end]=s[end],s[start]
#         start=start+1
#         end-=1
    
# s="We are ready"
# s=list(s)
# start=0
# while True:
#     try:
#         end=s.index(' ', start)
#         reverseword(s,start,end-1)
#         start=end+1
#     except ValueError:
#         reverseword(s,start,len(s)-1)
#         break
# s.reverse()
# s="".join(s)
# print(s)
