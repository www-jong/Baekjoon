N=int(input())
li=list(map(int,input().split()))
res=0
for i in li:
    if i==N:res+=1
print(res)
