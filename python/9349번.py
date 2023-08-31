T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    r=0
    while K*(r+1)-r<=N:
        r+=1
    print(r-1)