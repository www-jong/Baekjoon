N,M,K=map(int,input().split())
li=[[0]*(M+1)]
res=0
def check(y,x):
    white_start=[0,0]
    black_start=[0,0]
    tick=0
    for i in range(x,x+K):
        for j in range(y,y+K):
            if tick==0:
                if li[j][i]=='W':
                    white_start[0]+=1
                if li[j][i]=='B':
                    black_start[0]+=1
                tick=1
            else:
                if li[j][i]=='B':
                    white_start[1]+=1
                if li[j][i]=='W':
                    black_start[1]+=1
                tick=0
        if K%2==0:
            if tick==1:
                tick=0
            else:
                tick=1
    return max(sum(white_start),sum(black_start))

for i in range(N):
    li.append([0]+list(input()))
for i in range(1,N+1-K+1):
    for j in range(1,M+1-K+1):
        tmp=check(i,j)
        res=max(res,tmp)
print(K**2-res)
