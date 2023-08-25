def bs(tar):
    st=0
    end=len(dp)-1
    mid=(st+end)//2
    while st<=end:
        mid=(st+end)//2
        if dp[mid]<tar:
            st=mid+1
        elif dp[mid]>tar:
            end=mid-1
        else:
            return mid
    return st

n=int(input())
a=list(map(int,input().split()))
dp=[a[0]]
v=[0]

for i in range(1,n):
    if a[i]>dp[-1]:
        dp.append(a[i])
        v.append(len(dp)-1)
    else:
        idx=bs(a[i])
        v.append(idx)
        dp[idx]=a[i]
g=[]
idx=len(dp)-1
for i in range(len(v)-1,-1,-1):
    if v[i]==idx:
        g.append(a[i])
        idx-=1
print(len(dp))
print(*sorted(g))