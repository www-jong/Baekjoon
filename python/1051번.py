N,M=map(int,input().split())
li=[[0]*(M+1)]
for i in range(N):
    tmp=[0]+[int(i) for i in input()]
    li.append(tmp)
def check(x,y):
    tmp=1
    for i in range(1,min(N-x+1,M-y+1)):
        a=li[x][y]
        b=li[x][y+i]
        c=li[x+i][y]
        d=li[x+i][y+i]
        if a==b==c==d:
            tmp=max(tmp,(i+1)**2)
    return tmp

res=1
for x in range(1,N+1):
    for y in range(1,M+1):
        res=max(check(x,y),res)
print(res)