_=int(input())
li=map(int,input().split())
ans=0
v=int(input())
for i in li:
    if i==v:
        ans+=1
print(ans)