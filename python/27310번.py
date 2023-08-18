s=input()
res=len(s)
for i in s:
    if i==':':res+=1
    elif i=='_':res+=5
print(res)