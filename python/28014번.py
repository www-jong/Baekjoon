N=int(input())
li=list(map(int,input().split()))
r=0
n=0
for i in li:
    if i>=n:
        n=i
        r+=1
    else:
        n=i
print(r)