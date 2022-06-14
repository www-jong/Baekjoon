n=input().replace('()','l')
li=[]
ans=0
for i in n:
    if i=="(":
        li.append(1)
        ans+=1
    elif i=="l":
        ans+=len(li)
    else:
        li.pop()
print(ans)