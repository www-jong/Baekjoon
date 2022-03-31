import math
a=list(input())
s=[0]*10
for i in a:
    g=9 if int(i)==9 or int(i)==6 else int(i) 
    s[g]+=1
s[9]=math.ceil(s[9]/2)
print(max(s))