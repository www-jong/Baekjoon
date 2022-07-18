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
i,t=0,0
while i<=n:
    t=0
    if check[i]<gas[i]:
        tmp=road[i]
        for j in range(i+1,n):
            if gas[j]>gas[i]:
                tmp+=road[j]
                t+=1
            else:
                break
        ans+=tmp*gas[i]
    else:
        ans+=sum(road[i:])*gas[i]
        break
    i+=1+t
print(ans)