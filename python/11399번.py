n=int(input())
li=list(map(int,input().split()))
li.sort()
ans=0
for i in range(n):
    ans+=(n-i)*li[i]
print(ans)
print(li)