s=input()
ans=0
temp="-1"
for i in s:
    if temp=="-1":
        temp=i
        ans+=10
    else:
        if temp==i:
            ans+=5
            temp=i
        else:
            ans+=10
            temp=i
            
print(ans)