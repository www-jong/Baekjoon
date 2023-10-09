K,N=map(int,input().split())
if N==1:print(-1)
else:
    r=(K*N)//(N-1)
    if (K*N)%(N-1):r+=1
    print(r)