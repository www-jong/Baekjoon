count=0
N=int(input())
li=list(map(int,input().split()))
res=0
for i in li:
    if i!=0:
        count+=1
        res+=count
    else:
        count=0
print(res)