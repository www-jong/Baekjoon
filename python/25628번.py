N=int(input())
res=10000
for i in range(N):
    A,B=map(int,input().split())
    if A<=B:
        res=min(B,res)
if res==10000:
    print('-1')
else:
    print(res)