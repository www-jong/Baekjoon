import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))

def func(x,y,n):
    if n==2:
        tmp=[]
        for i in range(n):
            for j in range(n):
                tmp.append(li[x+i][y+j])
        return sorted(tmp)[1]
    a=func(x,y,n//2)
    b=func(x,y+n//2,n//2)
    c=func(x+n//2,y,n//2)
    d=func(x+n//2,y+n//2,n//2)
    return sorted([a,b,c,d])[1]

if N==1:
    print(*li[0])
else:
    print(func(0,0,N))