N=int(input())
li=list(map(int,input().split()))
res=0
for i in range(N-1):
    res+=abs(li[i]-li[i+1])**2+(li[i]+li[i+1])**2
print(res)