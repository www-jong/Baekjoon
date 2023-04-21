T=int(input())
li=list(map(int,input().split()))
r=0
for i in li:
    if i==T:
        r+=1
print(r)