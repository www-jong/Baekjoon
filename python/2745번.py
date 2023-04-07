N,B=map(str,input().split())
S,res,c=[],0,0
for i in N:
    if ord(i)>=65 and ord(i)<=90:
        S.append(str(ord(i)-55))
    else:
        S.append(i)

for i in S[::-1]:
    res+=int(i)*int(B)**c
    c+=1
print(res)