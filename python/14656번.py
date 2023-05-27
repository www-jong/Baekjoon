N=int(input())
li=list(map(int,input().split()))
res=0
for i in range(N):
    if li[i]!=i+1:
        res+=1
print(res)