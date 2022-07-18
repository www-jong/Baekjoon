n=int(input())
road=list(map(int,input().split()))
check=[0]*(n)
gas=list(map(int,input().split()))
ans,tmp=0,10000000000
for i in range(n-2,-1,-1):
    if gas[i]<tmp:
        tmp=gas[i]
        check[i]=tmp
    else:
        check[i]=tmp
#print(check)
for i in range(n):
    if check[i]<gas[i]:
        ans+=road[i]*gas[i]
    else:
        ans+=sum(road[i:])*gas[i]
        break
print(ans)