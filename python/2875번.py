N,M,K=map(int,input().split())
r=0
while True:
    if N<2 or M<1 or (M+N-3)<K:
        break
    r+=1
    N-=2
    M-=1
print(r)