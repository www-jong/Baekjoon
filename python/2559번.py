n,k=map(int,input().split())
li=[0]+list(map(int,input().split()))
max=sum(li[1:k+1])
now=sum(li[1:k+1])
s=1
e=k
while e<n:
    e+=1
    now=now+li[e]-li[s]
    if now>max:
        max=now
    s+=1
print(max)