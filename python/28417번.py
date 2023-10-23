N=int(input())
r=0
for i in range(N):
    li=list(map(int,input().split()))
    r=max(r,max(li[:2])+sum(sorted(li[2:],reverse=True)[:2]))
print(r)