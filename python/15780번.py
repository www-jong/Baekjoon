N,K=map(int,input().split())
li=list(map(int,input().split()))
r=sum([i//2+(1 if i%2 else 0) for i in li])
if r>=N:
    print("YES")
else:
    print("NO")